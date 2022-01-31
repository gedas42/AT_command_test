import configuration
import modules.command_line_parser as parsers
import modules.mailSender as email
import time

def ArgumentParser():
    parse = parsers.parser()
    return  parse

def ConfigLoad():
    parser=ArgumentParser()
    config=configuration.config(parser.getParsedArgs())
    mailConfig=config.getMailConfig()
    deviceConfig=config.getDeviceConfig()  
    return deviceConfig,mailConfig

def dynamin_module_upload(deviceConfig):
    try:
        module = __import__('modules.{type}Connection'.format(type=deviceConfig['connection']), fromlist=['modules'])
        return module
    except Exception as ex :
        print(ex)

def main():
    deviceConfig,mailConfig=ConfigLoad()
    module=dynamin_module_upload(deviceConfig)

    if deviceConfig['connection']=='serial':
        try:
            connection=module.loginSerial(deviceConfig['serialPort'],deviceConfig['baudRate'],deviceConfig)
            email.mail(mailConfig,"Device {} test was successful".format(deviceConfig['device']))
        except Exception as e:
            print(e)
            print("Could not connect to device")
            email.mail(mailConfig,"Device {} test failed".format(deviceConfig['device']))
        # connection.sendMessage()
    elif deviceConfig['connection']=='ssh':
        
        try:
            connection=module.loginSSH(deviceConfig)
            email.mail(mailConfig,"Device {} test was successful".format(deviceConfig['device']))
        except Exception as e:
            print(e)
            print("Could not connect to device") 
            email.mail(mailConfig,"Device {} test failed".format(deviceConfig['device']))       
    
 
if __name__ == "__main__":
    main()

