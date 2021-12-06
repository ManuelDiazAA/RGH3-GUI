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
        print(config)
        self.motherboard = config['motherboard']
        self.binPath = config['bin_path']
        self.cpuKey = config['cpu_key']
    
    def startCoverse( self ):
        print(
            self.motherboard,
            self.binPath,
            self.cpuKey,
        )