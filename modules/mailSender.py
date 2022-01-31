import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class mail:
    def __init__(self,config,message):
        self.config =config
        self.sendMail(message)
        

    def sendMail(self,text):
        mail_content = text
        sender_address = self.config['login']
        sender_pass = self.config['password']
        receiver_address = self.config['recipient']
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A test mail'   
        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP(self.config['smtp'], self.config['port']) 
        session.starttls() 
        session.login(sender_address, sender_pass) 
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')