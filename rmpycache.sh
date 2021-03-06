#!/usr/bin/env bash

if [[ "$(pwd)" == *"pyz-shell"* ]]; then
    pycachedirs=(
        src/__pycache__
        src/pluginmgr/__pycache__
        src/shell/__pycache__
        src/updatemgr/__pycache__
        src/pyziniter/__pycache__
        src/api/__pycache__
    )
    rm -r ${pycachedirs[*]}
else
    printf "Run in the project's directory\n"
    exit 1

fi
