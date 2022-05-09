#!/usr/bin/env bash

# You have been bamboozled.
# This is not a real make file, but rather
# a build/install script written in bash

versionstring="pyz_1.0.0_amd64"
debcontrol="Package: pyz
Version: 1.0.0
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
Icon=PyZlogo
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
- docs: Builds the man pages

- install: Builds the program and installs it to ~./local/bin
- update: Updates the program
- uninstall: If you've installed PyZ with ./make install, use this to uninstall it

- installdeps: Installs dependencies
    - all: Installs all dependencies
    - dev: Installs dependencies only required for development/compiling
    - runtime: Installs dependencies only required for runtime

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
        
        pythonfiles=(
            ../../src/main.py
            ../../src/shell/__init__.py
            ../../src/shell/shell.py
            ../../src/shell/rccreator.py
            ../../src/shell/pluginimport.py
            ../../src/pluginmgr/__init__.py
            ../../src/pluginmgr/manager.py
            ../../src/pluginmgr/installer.py
            ../../src/pluginmgr/mgrinit.py
            ../../src/pluginmgr/remover.py
            ../../src/pluginmgr/searcher.py
            ../../src/pluginmgr/updater.py
            ../../src/updatemgr/__init__.py
            ../../src/updatemgr/checker.py
            ../../src/pyziniter/__init__.py
            ../../src/pyziniter/pyzinit.py
            ../../src/pyziniter/verJSONcreate.py
        )

        pyinstaller --onefile "${pythonfiles[@]}"
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
    cp "pyz" "$HOME/.local/bin/pyz"
    cd ../../ || exit 1
    rm -r bin

    printf "[OK] Program installed!\n"
}

update () {
    build
    rm "$HOME/.local/bin/pyz"
    cp "pyz" "$HOME/.local/bin/pyz"

    wget https://raw.githubusercontent.com/CodyMarkix/PyZ-shell/master/version.json -O "$HOME/.local/share/pyz/version.json"
}

uninstall () {
    printf "Removing ~/.local/share/pyz..."
    rm -r "$HOME/.local/share/pyz"

    printf "Removing ~/.local/bin/pyz..."
    rm -r "$HOME/.local/bin/pyz"
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

docs () {
    cd src/docs || exit 1
    pandoc pyz.1.MD -s -t man -o pyz.1
    pandoc pyz-plugm.1.MD -s -t man -o pyz-plugm.1

    gzip pyz.1 && gzip pyz-plugm.1
    sudo --prompt="Enter your password (for moving the man-pages to a write-protected location): " mv pyz.1.gz /usr/local/share/man/man1/pyz.1.gz
    sudo mv pyz-plugm.1.gz /usr/local/share/man/man1/pyz-plugm.1.gz
    sudo mandb
}

installdeps () {
    if [[ "$1" == "all" ]]; then
        sudo apt install python3-pip pandoc || sudo pacman -S python-pip pandoc || sudo dnf install python3-pip pandoc
        pip install termcolor
        pip install pyinstaller
    
    elif [[ "$1" == "dev" ]]; then
        sudo apt install python3-pip pandoc || sudo pacman -S python-pip pandoc || sudo dnf install python3-pip pandoc
        pip install pyinstaller
    
    elif [[ "$1" == "runtime" ]]; then
        sudo apt install python3-pip || sudo pacman -S python-pip || sudo dnf install python3-pip
        pip install termcolor
    fi
}

main () {
    if [[ "$1" == "help" ]]; then
        help
    
    elif [[ "$1" == "build" ]]; then
        checkdeps
    
    elif [[ "$1" == "docs" ]]; then
        docs

    elif [[ "$1" == "install" ]]; then
        install

    elif [[ "$1" == "update" ]]; then
        update
    
    elif [[ "$1" == "uninstall" ]]; then
        uninstall

    elif [[ "$1" == "installdeps" ]]; then
        installdeps "$2"

    elif [[ "$1" == "package" ]]; then
        package "$2"
    
    elif [[ "$1" == "help" ]]; then
        help

    else
        help
    fi
}

main "$1" "$2" "$3"