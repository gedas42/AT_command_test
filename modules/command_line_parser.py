import argparse

class parser:

    def __init__(self):
        self.setParserRules()

    def setParserRules(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-p","--product", type=str,help="Enter test product name")

    def getParsedArgs(self):
        self.args = self.parser.parse_args() 

        return self.args.product

    

 


