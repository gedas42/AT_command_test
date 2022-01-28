import time
import colorama


class terminalWriter:
    def __init__(self,data):
        self.data = data
        self.passed=0
        self.failed=0

    def printDeviceTerminal(self):
        print("Testing {} device with {} connection\n".format(self.data['device'],self.data['connection']) )

    def printTestsTerminal(self,command,out,expected):
        if self.data['connection']=='ssh':
            result=out[len(out)-2]
        elif self.data['connection']=='serial':
            result=out[len(out)-1].decode('utf-8').strip()
        if result==expected:
            msg="Tested command {}".format(command)+", Test Results:"+f"{colorama.Fore.GREEN}" + "Passed" +f"{colorama.Style.RESET_ALL}"
            print("\033[A ",end = "\r")
            print('\r' + ' '*len(msg),end = "\r")
            print(msg,end = "\n",flush=True)
            self.passed+=1
        elif result!=expected:
            msg="Tested command {}".format(command)+", Test Results:"+f"{colorama.Fore.RED}" + "Failed" +f"{colorama.Style.RESET_ALL}"
            print("\033[A ",end = "\r")
            print('\r' + ' '*len(msg),end = "\r")
            print(msg,end = "\n",flush=True)
            self.failed+=1

    def printTestStatistics(self,tests):
        completed=self.failed+self.passed
        msg="{} tests completed out of {} tests".format(completed,tests)
        print(msg,flush=True)
        msg2=f"{colorama.Fore.GREEN}"+"{} tests succeeded, ".format(self.passed)+f"{colorama.Fore.RED}" + " {} failed".format(self.failed)+f"{colorama.Style.RESET_ALL}"
        print(msg2,flush=True)
        time.sleep(2)
        if completed!=tests:
            print("\033[A ",end = "\r")
            print('\r' + ' '*len(msg2),end = "\r")
            print("\033[A ",end = "\r")
            print('\r' + ' '*len(msg),end = "\r")

