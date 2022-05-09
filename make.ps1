#!/usr/bin/env pwsh

# You have been bamboozled.
# This is not a real make file, but rather
# a build/install script written in powershell

$helptext = "Help menu for PyZ's make script

Commands
- build: Builds the program and nothing else
- install: Builds the program and installs it to %USERPROFILE%\Appdata\PyZ
- update: Updates the program

- installdeps: Installs dependencies
    - all: Installs all dependencies
    - dev: Installs dependencies only required for development/compiling
    - runtime: Installs dependencies only required for runtime

    - help: Shows this help menu
"

function installPython() {
    if ("$(wmic os get osarchitecture)" -like '*64*' ) {
        Invoke-WebRequest "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe" -OutFile "$Env:Temp\pythoninstaller.exe"
        Invoke-Expression -Command "$Env:Temp\pythoninstaller.exe"
    } else {
        Invoke-WebRequest "https://www.python.org/ftp/python/3.10.4/python-3.10.4.exe" -OutFile "$Env:Temp\pythoninstaller.exe"
        Invoke-Expression -Command "$Env:Temp\pythoninstaller.exe"
    }
}

function makeShortcut () {
    $WshShell = New-Object -comObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($args[0])
    $Shortcut.TargetPath = $args[1]
    $Shortcut.Save()
}

function help () {
    Write-Host "$helptext"
}

function build () {
    mkdir -p bin\Windows
    Set-Location bin\Windows

    pyinstaller --onefile ..\..\src\main.py ..\..\src\shell\shell.py ..\..\src\shell\rccreator.py ..\..\src\pluginmgr\manager.py ..\..\src\shell\pluginimport.py ..\..\src\pluginmgr\installer.py ..\..\src\pluginmgr\mgrinit.py ..\..\src\pluginmgr\remover.py ..\..\src\pluginmgr\searcher.py ..\..\src\pluginmgr\updater.py

    Set-Location -Path dist
    Rename-Item -Path main.exe pyz.exe
    Move-Item -Path .\pyz.exe -Destination ..\pyz.exe

    Set-Location -Path ..
    Remove-Item -Confirm build
    Remove-Item dist
    Remove-Item main.spec
}
function install () {
    build

    New-Item -Path "$Env:USERPROFILE\AppData\Roaming" -Name "PyZ" -ItemType "directory"
    Move-Item -Path .\pyz.exe -Destination "$Env:USERPROFILE\AppData\Roaming\PyZ\pyz.exe"

    $Env:PATH += ";$Env:USERPROFILE\AppData\Roaming\PyZ"
    makeShortcut "$Env:AppData\Microsoft\Windows\Start Menu\Programs\PyZ.lnk" "$Env:USERPROFILE\AppData\Roaming\PyZ\pyz.exe"
}

function update () {
    build
    Remove-Item -Path "$Env:AppData\PyZ\pyz.exe"
    Copy-Item -Path ".\pyz.exe" -Destination "$Env:AppData\PyZ\pyt.exe"

    Invoke-WebRequest "https://raw.githubusercontent.com/CodyMarkix/PyZ-shell/master/version.json" -OutFile "$Env:AppData\PyZ\version.json"
}

function uninstall () {
    Remove-Item -Path "$Env:AppData\PyZ"
    Remove-Item -Path "$Env:AppData\Microsoft\Windows\Start Menu\Programs\PyZ.lnk"
    
    Write-Host "Uninstalled!"
    # If anyone knows how to remove a path from PATH, lmk please
}

function installdeps () {
    if ($args[0] -eq "all") {
        installPython
        pip install termcolor
        pip install pyinstaller

    } elseif ($args[0] -eq "dev") {
        installPython
        pip install pyinstaller

    } elseif ($args[0] -eq "runtime") {
        installPython
        pip install termcolor
    }
}

if ($args[0] -eq "help") {
    help
} elseif ($args[0] -eq "build") {
    build
} elseif ($args[0] -eq "install") {
    install
} elseif ($args[0] -eq "installdeps") {
    installdeps $args[1]
} elseif ($args[0] -eq "update") {
    update
} else {
    help
}