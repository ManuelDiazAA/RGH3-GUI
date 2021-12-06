from tkinter import *
from gui.controllers.rgh3ScriptController import Rgh3ScriptController

class ComponentButtonGenerateBin:
    
    def __init__( self, mainSelf ):
        self.mainSelf = mainSelf
        self.buttonGenerateBinLabel( )
        self.buttonGenerateBinTextBox( )
        self.buttonGenerateBinButton( )
        

    def buttonGenerateBinLabel( self ):
        pass

    def buttonGenerateBinTextBox( self ):
        pass

    def buttonGenerateBinButton( self ):
        buttonGenerateBinButton = Button(
            self.mainSelf.raiz,
            text = 'Generate .BIN',
            command = self.buttonGenerateBinPushEvent,
        )
        buttonGenerateBinButton.pack()

    def buttonGenerateBinPushEvent( self ):
        rgh3ScripObject = Rgh3ScriptController(
            config = {
                'motherboard': self.mainSelf.motherboard.motherBoardText.get(),
                'bin_path': self.mainSelf.bin.binText.get(),
                'cpu_key': self.mainSelf.cpu_key.cpuKeyText.get(),
            }
        )

        rgh3ScripObject.startConverse()