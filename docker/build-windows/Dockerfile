# escape=`

FROM microsoft/windowsservercore
#FROM microsoft/nanoserver

# Install chocolatey
RUN @powershell -NoProfile -ExecutionPolicy unrestricted -Command "(iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))) >$null 2>&1"

# Install Visual C++ Build Tools, as per: https://chocolatey.org/packages/visualcpp-build-tools
RUN choco install visualcpp-build-tools --version 14.0.25420.1 -y

# Add msbuild to PATH
RUN setx /M PATH "%PATH%;C:\Program Files (x86)\MSBuild\14.0\bin"

# Test msbuild can be accessed without path
RUN msbuild -version

# Add python to the image
RUN choco install python --version 3.6.6 -y
RUN choco install git -y

# Set the Workdir
WORKDIR C:\workdir

# Default to PowerShell if no other command specified.
CMD ["powershell.exe", "-NoLogo", "-ExecutionPolicy", "Bypass"]

RUN pip install wheel
ADD requirements.txt C:\requirements.txt
RUN pip install -r C:\requirements.txt

ADD . C:\workdir






# escape=`

# Use the latest Windows Server Core image with .NET Framework 4.7.1.
#FROM microsoft/dotnet-framework:4.7.1

# Restore the default Windows shell for correct batch processing below.
#SHELL ["cmd", "/S", "/C"]

# Download the Build Tools bootstrapper.
#ADD https://aka.ms/vs/15/release/vs_buildtools.exe C:\TEMP\vs_buildtools.exe

# Install Build Tools excluding workloads and components with known issues.
#RUN C:\TEMP\vs_buildtools.exe --quiet --wait --norestart --nocache `
#    --installPath C:\BuildTools `
#    --all `
#    --remove Microsoft.VisualStudio.Component.Windows10SDK.10240 `
#    --remove Microsoft.VisualStudio.Component.Windows10SDK.10586 `
#    --remove Microsoft.VisualStudio.Component.Windows10SDK.14393 `
#    --remove Microsoft.VisualStudio.Component.Windows81SDK `
# || IF "%ERRORLEVEL%"=="3010" EXIT 0

# Start developer command prompt with any other commands specified.
#ENTRYPOINT C:\BuildTools\Common7\Tools\VsDevCmd.bat &&

# Default to PowerShell if no other command specified.
#CMD ["powershell.exe", "-NoLogo", "-ExecutionPolicy", "Bypass"]