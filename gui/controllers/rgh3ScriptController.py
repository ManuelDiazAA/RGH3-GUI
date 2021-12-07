import subprocess
import sys
import os 
from gui.controllers.rgh3Script.twotothree import TwoToThree

class Rgh3ScriptController:
    def __init__( self, config ):
        """Config is a dict and get:
            {
                motherboard: [int], is the type of x360board.-
                    example:
                        1.- Corona
                        2.- Jasper
                        3.- Falcon
                        4.- Trinity
                bin_path: [string], is the path of the bin file
                cpu_key: [string], is the cpu_key
            }
        """
        self.motherboard = config['motherboard']
        self.binPath = config['bin_path']
        self.cpuKey = config['cpu_key']
    
    def startConverse( self ):

        if self.motherboard == 'Corona':
            motherboard_path = '/rgh3Script/motherBoards/Corona/RGH3_Corona.bin'
        if self.motherboard == 'Corona 4GB':
            motherboard_path = '/rgh3Script/motherBoards/Corona/RGH3_Corona_4G.bin'
        if self.motherboard == 'Falcon 10MHZ':
            motherboard_path = '/rgh3Script/motherBoards/Falcon/RGH3_Falcon_10mhz.bin'
        if self.motherboard == 'Falcon 27MHZ':
            motherboard_path = '/rgh3Script/motherBoards/Falcon/RGH3_Falcon_27mhz.bin'
        if self.motherboard == 'Jasper 10mhz':
            motherboard_path = '/rgh3Script/motherBoards/Jasper/RGH3_Jasper_10mhz.bin'
        if self.motherboard == 'Jasper 27mhz':
            motherboard_path = '/rgh3Script/motherBoards/Jasper/RGH3_Jasper_27mhz.bin'
        if self.motherboard == 'Jasper64 10mhz':
            motherboard_path = '/rgh3Script/motherBoards/Jasper/RGH3_Jasper64_10mhz.bin'
        if self.motherboard == 'Jasper64 27mhz':
            motherboard_path = '/rgh3Script/motherBoards/Jasper/RGH3_Jasper64_27mhz.bin'
        if self.motherboard == 'Trinity':
            motherboard_path = '/rgh3Script/motherBoards/Trinity/RGH3_Trinity.bin'

        ecc_path = os.path.dirname(os.path.realpath(__file__)) + motherboard_path
        print(ecc_path)
        if not os.path.isfile( ecc_path ):
            raise Exception('Archivo ECC Motherboard no encontrado')

        convert_process = TwoToThree(
            config={
                'rgh3_ecc' : ecc_path,
                'updflash' : self.binPath,
                'cpu_key' : self.cpuKey,
            }
        )

        convert_process.start_encrypt()
