from datetime import datetime
import csv

class csvObj:
    
    def __init__(self,data,header):
        self.data = data
        self.openCsv()
        self.header = header

    def openCsv(self):
        self.file1 = open("Results/results"+self.data['device']+str(datetime.now())+".csv" ,"w",encoding='utf-8')
        self.writer = csv.writer(self.file1)
 

    def appendCsv(self,output):
        list=[]
        self.writer.writerow(self.data['device'].splitlines())
        for i in range(len(self.header)):
            self.writer.writerow(self.header[i].splitlines())
        header=['Command','args','ExpectedResults','Results',"TestResults"]
        self.writer.writerow(header)  
        for line in self.data["commands"]:
            if self.data['connection']=='serial':
                result=output[len(output)-1].decode('utf-8').strip()
            elif self.data['connection']=='ssh':
                result=output
            
            if result==line["ExpectedResults"]:
                test='Passed'
            else:
                test= 'Failed'
            list.append([line["command"],line["arg"],line["ExpectedResults"],result,test])

        self.writer.writerows(list)

    def closeCsv(self):
        self.file1.close()
    
