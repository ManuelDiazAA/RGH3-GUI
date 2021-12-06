from tkinter import *
from gui.components.componentBin import ComponentBin
from gui.components.componentCpuKey import ComponentCpuKey
from gui.components.componentMotherBoard import ComponentMotherBoard
from gui.components.componentButtonGenerateBin import ComponentButtonGenerateBin

class rgh3Gui:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('RGH3.0 - GUIs')
        self.raiz.resizable(0,0)
        self.mainFrame()

    def mainFrame(self):
        self.main = Frame(
            self.raiz, \
            width=600,
            height=330,
            #background='blue'
            )

        self.main.pack()

        self.bin = ComponentBin( self )
        self.cpu_key = ComponentCpuKey( self )
        self.motherboard = ComponentMotherBoard( self )
        self.generateBinButton = ComponentButtonGenerateBin( self )

    def start(self):
        self.raiz.mainloop()
    
    def generateBin( self ):
        pass

