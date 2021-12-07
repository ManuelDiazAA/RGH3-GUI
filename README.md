# RGH3-GUI
Gui creada para facilitar el uso del script para RGH3 

author del script original RGH2 to 3 by DrSchottky

####################### version 0.1 #########################

dependencias:
    1.- tkinter : sudo apt-install python3-tk
    2.- pycrypto : python3 -m pip install pycryptodome pyinstaller

ejecutar: "python main.py" desde la raiz de este proyecto

build:
    1.- copiar hook-Crypto.py en carpeta hooks de pyinstaller
    2.- ejecutar: "python3 -m pyinstaller --windowed --onefile main.py"
    3.- copiar carpeta "public" y "motherBoards" ah "dist"

el ejecutable se encuentra en la carpeta dist

