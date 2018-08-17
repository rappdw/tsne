$scriptPath = (Get-Item (Split-Path $MyInvocation.MyCommand.Path)).Parent.FullName
Set-Location $scriptPath

if (Test-Path $scriptPath\dist) {
    echo "`n*** Cleaning up dist folder ***"
    rm dist\*
}

echo "`n*** Running bdist_wheel ***"
python setup.py bdist_wheel

if (Test-Path $scriptPath\distout\) {
    echo "`n*** Copying the files from dist\ to distout\ ***"
    cp dist\* distout\

    echo "`n*** All done, listing built wheels ***"
    ls distout\
}
else 
{
    echo "`n*** All done, listing built wheels ***"
    ls dist\
}
