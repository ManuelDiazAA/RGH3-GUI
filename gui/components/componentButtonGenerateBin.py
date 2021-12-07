import os
from tkinter import *
from tkinter import messagebox
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
        try:
            if self.mainSelf.bin.binText.get() == '':
                raise Exception('El campo Nand no puede estar vacio')
            if not os.path.isfile( self.mainSelf.bin.binText.get() ):
                raise Exception('Archivo Nand no encontrado')
            if self.mainSelf.cpu_key.cpuKeyText.get() == '':
                raise Exception('El campo CPUKEY no puede estar vacio')
            try:
                cpu_key_hex = bytearray.fromhex(self.mainSelf.cpu_key.cpuKeyText.get())
            except:
                raise Exception('Formato CPU_KEY incorrecto')
            if len(cpu_key_hex) != 16:
                raise Exception('Tamano CPU_KEY incorrecto')
            
            rgh3ScripObject = Rgh3ScriptController(
                config = {
                    'motherboard': self.mainSelf.motherboard.motherBoardText.get(),
                    'bin_path': self.mainSelf.bin.binText.get(),
                    'cpu_key': self.mainSelf.cpu_key.cpuKeyText.get(),
                }
            )

            rgh3ScripObject.startConverse()

            messagebox.showinfo(title='Success', message='Done! search nand.bin in public/output')
        
        except Exception as e:
            messagebox.showerror(title='Error', message=e)
