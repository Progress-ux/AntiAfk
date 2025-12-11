# AntiAfk

## Instructions for Windows PowerShell

### Clone repository
```sh
git clone https://github.com/Progress-ux/AntiAfk.git
cd AntiAfk
```
### Create venv
```sh
python -m venv venv
.\venv\Scripts\Activate.ps1
```
### Add dependencies
```sh
pip install keyboard 
```

## If you want to compile in exe
### Install pyinstaller
```sh
pip install pyinstaller
```
### Compile in exe
```sh
pyinstaller --onefile --noconsole --name BoberLob --icon "data//BoberLobIco.ico" --add-data "data//BoberLobIco.ico;." main.py
```

### Possible commands to resolve errors
```sh
Set-ExecutionPolicy RemoteSigned
```