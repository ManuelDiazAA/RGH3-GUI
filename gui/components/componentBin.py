from tkinter import *
from tkinter.filedialog import askopenfilename

class ComponentBin:
    binText = ''
    def __init__( self, mainSelf ):
        #Set main object
        self.mainSelf = mainSelf
        #Set object vars
        self.binText = StringVar()
        #Init components 
        self.binLabel( )
        self.binTextBox( )
        self.binButton( )
        

    def binLabel( self ):
        binLabel = Label(
            self.mainSelf.main,
            text = '.BIN: ',
            )
        binLabel.grid(
            row = 0,
            column = 0,
            sticky='w',
            padx=10,
            pady=10,
        )

    def binTextBox( self ):
        binTextBox = Entry(
            self.mainSelf.main,
            textvariable = self.binText
        )

        binTextBox.grid(
            row = 0,
            column = 1,
            padx=10,
            pady=10,
        )

    def binButton( self ):
        buttonBinButton = Button(
            self.mainSelf.main,
            text = '...',
            command = self.binButtonPushEvent,
        )

        buttonBinButton.grid(
            row = 0,
            column = 2,
            padx=10,
            pady=10,
        )
    
    def binButtonPushEvent( self ):
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        self.binText.set(filename)