param (
    [switch] $NoBuild, 
    [string] $ImageName = 'tsne-windows-build',
    [string] $ContainerName = 'tsne-py-wheel'
)

$scriptPath = (Get-Item (Split-Path $MyInvocation.MyCommand.Path)).Parent.FullName
Set-Location $scriptPath

if (-not $NoBuild) {
    echo "`n*** Building the docker image ***"
    docker build -t $ImageName -f .\docker\build-windows\Dockerfile .
}

echo "`n*** Deleting container if already exists ***"
docker rm -vf $ContainerName

echo "`n*** Build the windows python wheel (Output .\dist) ***"
docker run -it --name $ContainerName --mount type=bind,source=$scriptPath/dist,target=C:/workdir/distout `
               -v $scriptPath/.git:C:/workdir/.git `
               $ImageName powershell -Command 'bin\build.ps1'