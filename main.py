import configuration
import modules.command_line_parser as parsers


def ArgumentParser():
    parse = parsers.parser()
    return  parse

def ConfigLoad():
    parser=ArgumentParser()
    config=configuration.config(parser.getParsedArgs())
    deviceConfig=config.getDeviceConfig()  
    return deviceConfig

def dynamin_module_upload(deviceConfig):
    try:
        module = __import__('modules.{type}Connection'.format(type=deviceConfig['connection']), fromlist=['modules'])
        return module
    except Exception as ex :
        print(ex)

def main():
    deviceConfig=ConfigLoad()
    module=dynamin_module_upload(deviceConfig)

    if deviceConfig['connection']=='serial':
        try:
            connection=module.loginSerial(deviceConfig['serialPort'],deviceConfig['baudRate'],deviceConfig)
        except Exception as e:
            print(e)
            print("Could not connect to device")
        # connection.sendMessage()
    elif deviceConfig['connection']=='ssh':
        
        try:
            connection=module.loginSSH(deviceConfig)
        except Exception as e:
            print(e)
            print("Could not connect to device")        
    
 
if __name__ == "__main__":
    main()

