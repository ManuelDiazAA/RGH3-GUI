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
        self.motherBoardText = StringVar(self.mainSelf.main)
        choices = { 
            (1, 'Corona'),
            (2, 'Falcon'),
            (3, 'Jasper'),
            (4, 'Trinity',)
            }
        self.motherBoardText.set('Corona') # set the default option

        self.popupMenu = OptionMenu(
            self.mainSelf.main,
            self.motherBoardText,
            *choices)
        self.popupMenu.grid(row = 2, column =1)