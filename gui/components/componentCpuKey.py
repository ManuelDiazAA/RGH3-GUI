from tkinter import *

class ComponentCpuKey:
    cpuKeyText = ''


    def __init__( self, mainSelf ):
        self.mainSelf = mainSelf
        self.cpuKeyText = StringVar()
        self.cpuKeyLabel( )
        self.cpuKeyTextBox( )
        self.cpuKeyButton( )

    def cpuKeyLabel( self ):
        cpuKeyLabel = Label(
            self.mainSelf.main,
            text = 'Cpu-Key: '
            )
        cpuKeyLabel.grid(
            row = 1,
            column = 0,
            sticky='w',
            padx=10,
            pady=10,
        )

    def cpuKeyTextBox( self ):
        self.cpuKeyTextBox = Entry(
            self.mainSelf.main,
            textvariable = self.cpuKeyText
        )

        self.cpuKeyTextBox.grid(
            row = 1,
            column = 1,
            padx=10,
            pady=10,
        )

    def cpuKeyButton( self ):
        pass