import ftplib
class ftpserver:

    def __init__(self,filename,data):
        self.storeResults(filename,data)

    def storeResults(self,name,data):
        session = ftplib.FTP(data['server'],data['username'],data['password'])
        file = open(name,'rb')                  # file to send
        session.storbinary('STOR /home/'+data['username']+'/'+name[8:], file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()