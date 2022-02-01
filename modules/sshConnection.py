import paramiko
import time
import modules.csvWrite as csv
import modules.terminalWrite as terminal


class loginSSH:

    def __init__(self,data,ip,port,username,password):
        self.data=data
        self.createCon(ip,port,username,password)

    def createCon(self, host, port, username, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, port, username, password)
        self.__shell = self.ssh.invoke_shell()
        time.sleep(1)
    def stopGSMD(self):
        try:
            self.__shell.send("/etc/init.d/gsmd stop\r")
            time.sleep(1)            
        except Exception as e:
            print(e)
    def startGSMD(self):
        try:
            self.__shell.send("/etc/init.d/gsmd start\r")
            time.sleep(1)            
        except Exception as e:
            print(e)

    def executeTest(self):
        self.stopGSMD()
        self.__shell.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r")
        time.sleep(1)
        self.__shell.recv(9999) 
        self.execCommand()
        self.startGSMD()
        self.ssh.close()
        return self.filename

        

    def MakeDeviceHeaderCsv(self):
        self.__shell.send("ATI"+'\r')
        time.sleep(1)
        device=self.__shell.recv(9999).decode().splitlines()
        devicelist=[]
        for i in range(len(device)):
            if device[i]!="":
                devicelist.append(device[i])
        devicelist.pop()
        return devicelist

    def CreateCsv(self):
        header=self.MakeDeviceHeaderCsv()
        self.csvFile=csv.csvObj(self.data,header)

    def execCommand(self):
        self.CreateCsv()
        time.sleep(1)
        terminalPrint=terminal.terminalWriter(self.data)
        terminalPrint.printDeviceTerminal()
        for i in self.data['commands']:
            self.__shell.send(i['command']+'\r')
            if i['arg']!="":
                self.__shell.send(i['arg']+'\r')
            time.sleep(1)
            out=self.__shell.recv(9999).decode().splitlines()
            terminalPrint.printTestsTerminal(i['command'],out,i['ExpectedResults'])
            terminalPrint.printTestStatistics(len(self.data['commands']))
        print('')
        self.filename=self.csvFile.appendCsv(out[len(out)-2])       






