import argparse

class parser:

    def __init__(self):
        self.setParserRules()

    def setParserRules(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-d", "--device", type=str,help="Enter test device name",required=True)
        self.parser.add_argument("-i", "--ip", type=str,help="Enter test device IP address")
        self.parser.add_argument("-po", "--port", type=str,help="Enter test device port")
        self.parser.add_argument("-l", "--login", type=str,help="Enter test device login")
        self.parser.add_argument("-p", "--password", type=str,help="Enter test device password")
        self.parser.add_argument("-s", "--serialPort", type=str,help="Enter test device serial port")
        self.parser.add_argument("-b", "--baudRate", type=str,help="Enter test device baud rate")


    def getParsedArgs(self):
        self.args = self.parser.parse_args() 
        return self.args

    

 


