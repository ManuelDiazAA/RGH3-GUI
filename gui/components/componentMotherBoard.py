from tkinter import *

class ComponentMotherBoard:
    motherBoardText = ''

    def __init__( self, mainSelf ):
        self.mainSelf = mainSelf 
        self.motherBoardText = StringVar()
        self.motherBoardLabel( )
        self.motherBoardTextBox( )
        self.motherBoardButton( )
        self.motherBoardListBox( )

    def motherBoardLabel( self ):
        motherBoardLabel = Label(
            self.mainSelf.main,
            text = 'Motherboard: '
            )
        motherBoardLabel.grid(
            row = 2,
            column = 0,
            sticky='w',
            padx=10,
            pady=10,
        )

    def motherBoardTextBox( self ):
        pass

    def motherBoardButton( self ):
        pass

    def motherBoardListBox( self ):
        choices = [ 
            (1, 'Corona'),
            (2, 'Corona 4GB'),
            (3, 'Falcon 10MHZ'),
            (4, 'Falcon 27MHZ'),
            (5, 'Jasper 10mhz'),
            (6, 'Jasper 27mhz'),
            (7, 'Jasper64 10mhz'),
            (8, 'Jasper64 27mhz'),
            (9, 'Trinity',)
        ]
        self.motherBoardText.set((1, 'Corona')) # set the default option

        self.popupMenu = OptionMenu(
            self.mainSelf.main,
            self.motherBoardText,
            *choices,
            )
        self.popupMenu.grid(row = 2, column =1)