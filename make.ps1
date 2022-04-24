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
    if ( Get-Location -contains )
}

function install () {
    Write-Host "install"
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