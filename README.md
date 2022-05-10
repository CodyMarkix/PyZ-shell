<img class="container" src="icon/PyZlogo.png" width="150" height="150">

# PyZ - A custom shell for Python, written in Python

- - -

PyZ is meant to be a custom shell for python. Contains a customizable shell, a .rc file and perhaps more coming soon! The shell's main inspiration is zsh, an alternative shell to bash. Except instead of being an entire different programming language, it's an alternative shell!

- [PyZ - A custom shell for Python, written in Python](#pyz---a-custom-shell-for-python-written-in-python)
  - [Platform support](#platform-support)
  - [Installation with pre-built binary](#installation-with-pre-built-binary)
  - [Building from source](#building-from-source)
      - [Windows](#windows)
      - [Linux](#linux)
  - [Installing from source](#installing-from-source)
  - [Dependencies](#dependencies)
  - [Usage](#usage)
    - [Running the shell](#running-the-shell)
  - [Customization](#customization)
    - [.pyzrc file](#pyzrc-file)
    - [Prompt themes](#prompt-themes)
  - [Currently known bugs](#currently-known-bugs)
  - [To-do list](#to-do-list)

## Platform support

This being a Python app, it's able to work on basically anything that can run a python intrepreter. So

- Windows
- MacOS
- Linux
- Free/OpenBSD

and probably many more.

## Installation with pre-built binary

- Head over to the release tab and select the desired release

<img src="https://i.imgur.com/EMvQduv.png">

- Then choose the version of PyZ you want:

  - Windows users will want to download the .exe
  - Debian Linux users will want to download the .deb
  - Any Linux users will want to download the binary with no extension

- Download it and install it.

  - Debian:
    
    ```bash
    sudo apt install ./pyz_v1.0.0_amd64.deb
    ```

  - Linux binary:
  
    Open a terminal in the executable's directory and run
    ```bash
    cp pyz-1.0.0-x64 $HOME/.local/bin/pyz
    ```

  - Windows .exe:
  
    Open a terminal in the .exe's directory and run
    ```powershell
    New-Item -Path "$Env:AppData\Roaming" -Name "PyZ" -ItemType "directory" && Copy-Item -Path ".\pyz-v1.0.0-x64.exe" -Destination "$Env:AppData\Roaming\PyZ\PyZ.exe" && $Env:PATH += ";$Env:USERPROFILE\AppData\Roaming\PyZ"
    ```

## Building from source

- Clone the repository

```bash
git clone https://github.com/CodyMarkix/PyZ-Shell
```
- Then enter the cloned git repository and run the make script.

#### Windows
```
.\make.ps1 build
```

#### Linux
```
./make build
```

- The generated binary will either be in `bin/Linux` or `bin\Windows`.

## Installing from source

- Cd into the repository and run

```
./make help
```

or

```
.\make.ps1 help
```

- This will show the possible actions in the make script. On Linux, it's currently possible to:
  - Install a normal Linux binary to `~/.local/bin/` - `./make install`
  - Make a deb package (manual apt installation required) - `./make package deb`
  - Make an AppImage - `./make package appimage`

- On Windows, it's currently possible to:
  - Install a normal Windows binary to `%USERPROFILE%\AppData\Roaming\PyZ\` - `.\make.ps1 install`


## Dependencies

- Tested with Python 3.8.x (Theoretically should support up to 3.10.x)
- Termcolor
- Pyinstaller (for creating a binary!)
- AppImageTool (for creating an AppImage!)

## Usage

### Running the shell
- There's 3 ways to run the shell.

1. Open up a terminal and run `pyz`.
2. If you downloaded the AppImage and used something like AppImageLauncher to register it into your DE's menu, open that menu and click on "PyZ".
3. Open the Start Menu and select PyZ.

## Customization

### .pyzrc file
This is where a lot of the magic happens, customization-wise. In the default .rc file, there's a prompt decleration and some notes. You'll want to keep some sort of prompt.

By default, PyZ uses the Termcolor module, which is hard-imported, along with some others in the standard modules. But you can add whatever prompts you want.

### Prompt themes

As you may notice, the .pyzrc file is basically a script that is went through and is executed line-by-line when an instance of the shell is opened. Meaning you can have various prompts. Some examples include:

Bourpy (default):
```python
global prompt; prompt = "[ "+ termcolor.colored(os.getcwd(), "green") + " ]"+ termcolor.colored(" >", "blue")
```
Which produces:

<img src="https://i.imgur.com/i3RT4U3.png">

Classic:
```python
global prompt; prompt = "PyZ >>>"
```
Which produces:

<img src="https://i.imgur.com/09JzFRO.png">


## Currently known bugs

- Nested multi-line code is not supported

## To-do list

- [x] Complete make.ps1
- [x] Fix building from source
- [x] Fix multi-line code bug