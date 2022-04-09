#!/usr/bin/env bash

# You have been bamboozled.
# This is not a real make file, but rather
# a build/install script written in bash

versionstring="pyz_0.9_amd64"
debcontrol="Package: pyz
Version: 0.9
Architecture: amd64
Essential: no
Priority: optional
Depends: python3, python3-pip, sudo
Maintainer: Markix
Description: A shell, written in Python, for Python
"

desktopfile="[Desktop Entry]
Name=PyZ
Exec=pyz
Icon=PyZlogo.png
Type=Application
Terminal=true
Categories=Utility
"
apprun="#!/bin/sh

CURRDIR=\"\$(dirname \"\$(readlink -f \"\${0}\")\")\"
EXEC=\"\${CURRDIR}/usr/local/bin/pyz\"
exec \"\${EXEC}\""

helptext="Help menu for PyZ's make script

make [COMMAND]
make package [DEB/AppImage]

Commands:
- build: Builds the program and nothing else
- install: Builds the program and installs it to ~./local/bin
- installdeps: Installs necesarry dependencies
- package: Builds the program and creates a package
- help: Shows this help menu

"

help () {
    printf "%s" "$helptext"
}

build () {
    
    if [[ "$OSTYPE" == *"linux-gnu"* ]]; then
        mkdir -p bin/Linux
        cd bin/Linux || exit 2
        
        pyinstaller --onefile ../../src/main.py ../../src/shell/rccreator.py ../../src/shell/shell.py
        if [[ "$?" != "0" ]]; then
            printf "[ERROR] Error while building! Check logs above"
            exit 1
        else
            cd dist || exit 2
            mv main ../pyz
            
            cd ../ || exit 2
            rm -r build dist main.spec
            printf "[OK] Build successful!\n"
        fi
    else
        printf "[ERROR] Platform error! If you are on Windows, run make.ps1.\nIf you are on macOS, unfortunately, there is no binary for you.\n"
    fi
}

install () {
    build
    sudo --prompt="Enter your password to move to write-protected area (/usr/local/bin/):" cp "pyz" "/usr/local/bin/pyz"
    cd ../../.. || exit 1
    rm -r bin

    printf "[OK] Program installed!\n"
}

package () {
    if [[ "$1" == "DEB" ]] || [[ "$1" == "deb" ]]; then
        build
        
        cd ../ || exit 1
        mkdir -p "${versionstring}/DEBIAN" "${versionstring}/usr/local/bin"
        touch "${versionstring}/DEBIAN/control"
        echo "${debcontrol}" > ${versionstring}/DEBIAN/control
        
        cd Linux/ || exit 1
        cp "pyz" "../${versionstring}/usr/local/bin/pyz"
         
        cd ../ || exit 1
        dpkg-deb --build ${versionstring}

        rm -r "${versionstring}"
        mv "${versionstring}.deb" Linux/
        cd Linux/ || exit 1
    
    elif [[ "$1" == "AppImage" ]] || [[ "$1" == "Appimage" ]] || [[ "$1" == "appImage" ]] || [[ "$1" == "appimage" ]] || [[ "$1" == "APPIMAGE" ]]; then
        build

        cd ../ || exit 1
        mkdir "${versionstring}.AppDir" && cd "${versionstring}.AppDir" || exit 1
        mkdir -p usr/local/bin
        
        touch pyz.desktop
        echo "${desktopfile}" > pyz.desktop
        chmod +x pyz.desktop

        touch AppRun
        echo "${apprun}" > AppRun
        chmod +x AppRun

        cp ../../icon/PyZlogo.png ./PyZlogo.png

        cd ../Linux || exit 1
        cp "pyz" "../${versionstring}.AppDir/usr/local/bin/pyz"
        
        printf "\nUnfortunately for now, you have to run AppImageTool yourself.\nCopy the path to the %s.AppDir folder and run: ARCH=x86_64 /path/to/AppImageTool /path/to/AppDir/folder\n" "${versionstring}"

    else
        printf "[ERROR] Please specify what kind of package you want to create!\n"
    
    fi
}

checkdeps () {
    if [ "$(pip)" ]; then
        if [[ -n "$(pip list | grep -i termcolor)" ]]; then
            if [[ -n "$(pip list | grep -i pyinstaller)" ]]; then
                build
            else
                printf "[ERROR] Dependency error!\n\nThe pyinstaller module is required!\nInstall using \"pip install pyinstaller\"" || exit 1
            fi
        else
            printf "[ERROR] Dependency error!\n\nThe Termcolor module is required!\nInstall using \"pip install termcolor\"" || exit 1
        
        fi
    else
        printf "[ERROR] Dependency error!\n\nPython's PIP module manager required.\n" || exit 1
    
    fi
}

installdeps () {
    sudo apt install python3-pip
    pip install termcolor
    pip install pyinstaller
}

main () {
    if [[ "$1" == "help" ]]; then
        help
    
    elif [[ "$1" == "build" ]]; then
        checkdeps
    
    elif [[ "$1" == "install" ]]; then
        install
    
    elif [[ "$1" == "installdeps" ]]; then
        installdeps

    elif [[ "$1" == "package" ]]; then
        package "$2"
    
    elif [[ "$1" == "help" ]]; then
        help

    else
        help
    fi
}

main "$1" "$2" "$3"