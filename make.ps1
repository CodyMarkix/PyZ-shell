#!/usr/bin/env pwsh

# You have been bamboozled.
# This is not a real make file, but rather
# a build/install script written in powershell

$helptext = "Help menu for PyZ's make script

Commands
- build: Builds the program and nothing else
- install: Builds the program and installs it to ~./local/bin or %USERPROFILE%\Appdata\PyZ
- help: Shows this help menu
"

function help () {
    Write-Host "$helptext"
}

function build () {
    mkdir -p bin\Windows
    Set-Location bin\Windows

    C:\Users\WinVM\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\Scripts\pyinstaller.exe --onefile ..\..\src\main.py ..\..\src\shell\shell.py ..\..\src\shell\rccreator.py ..\..\src\pluginmgr\manager.py ..\..\src\shell\pluginimport.py ..\..\src\pluginmgr\installer.py ..\..\src\pluginmgr\mgrinit.py ..\..\src\pluginmgr\remover.py ..\..\src\pluginmgr\searcher.py ..\..\src\pluginmgr\updater.py

    Set-Location -Path dist
    Rename-Item -Path main.exe pyz.exe
    Move-Item -Path .\pyz.exe -Destination ..\pyz.exe

    Set-Location -Path ..
    Remove-Item -Confirm build
    Remove-Item dist
    Remove-Item main.spec

function install () {
    build

    New-Item -Path "C:\Program Files" -Name "PyZ" -ItemType "directory"
    Move-Item -Path .\pyz.exe -Destination "C:\Program Files\PyZ\pyz.exe"
}

if ($1 = "help") {
    help
} elseif ($1 = "build") {
    build
} elseif ($1 = "install") {
    install
} else {
    help
}