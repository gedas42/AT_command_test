import time
import serial
import os
import modules.csvWrite as csv
import modules.terminalWrite as terminal
from curses import ascii  


class loginSerial:

    def __init__(self,port,baud,data):
        self.data = data
        self.connect(port,baud)  


    def connect(self,port,baud):
        self.stopModemManager()
        self.ser = serial.Serial(port, baud, timeout=0.5)

    def stopModemManager(self):
        os.system("sudo systemctl stop ModemManager")

    def getCsvHeader(self):
        self.executeCommands("ATI")
        response=self.ser.readlines()
        header=[]
        for i in range(len(response)):
            if response[i].decode('utf-8').strip()!="":
                header.append(response[i].decode('utf-8').strip())
        header.pop()
        return header

    def sendCommands(self):
        header=self.getCsvHeader()
        self.csvFile=csv.csvObj(self.data,header)
        terminalPrint=terminal.terminalWriter(self.data)
        terminalPrint.printDeviceTerminal()
        time.sleep(1)
        for i in self.data['commands']:
            self.executeCommands(i['command'])
            if i['arg']:
                self.executeCommands(i['arg'])
            lines=self.ReadCommandResponse()
            terminalPrint.printTestsTerminal(i['command'],lines,i['ExpectedResults'])
            terminalPrint.printTestStatistics(len(self.data['commands']))
        self.fileName=self.csvFile.appendCsv(lines)
        self.disconnect()
        return self.fileName

    def executeCommands(self,command:str):
        self.ser.write(bytes(command+'\r', encoding='ascii'))  

    def ReadCommandResponse(self):
        lines=self.ser.readlines()
        return lines   
 
      
    def disconnect(self):
        self.ser.close()
        

