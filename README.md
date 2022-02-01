# AT_command_test

# Setup

Operating system Ubuntu 21.10

Python 3.6.9

# Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip3 install paramiko
pip3 install pyserial
```
# Configuration file

Configuration file is used to define devices with their connection type and the commands that will be tested on those devices. It must be named "data.json".

All information is stored inside "devices": json object array.
### For FTP configuration

 "server": server address

 "username":Login username for ftp server

 "password":Login password for ftp server

### For Mail configuration

 "login":email login name

 "password":email password

 "port": smtp port for selected email service

 "smtp": server for selected email smtp

 "recipient": recipient email address

### Device structure

#### For SSH connection device:

"device": Device name for which the configuration is being created.

"connection": Connection type that this device is using.

"commands":[] All AT commands for the specified device are stored inside commands array.

#### For serial connection device.

"device":Device name for which the configuration is being created.

"connection":Connection type

"commands":[] All AT commands for the specified device are stored inside commands array.

### Command structure

"command": AT command that will be tested

"param": Parameters for the command if needed, if not write "" with nothing inside.

"expectedOutput": Expected output of the modem command.

## Json example

```json

{
    "mail":{
        "login":"gon161gon@gmail.com",
        "password":"admin123.",
        "port":"587",
        "smtp":"smtp.gmail.com",
        "recipient":"gedas.kambaras@gmail.com"
        },

    "ftp":{
        "server":"iotacademy16",
        "username":"testuser",
        "password":"admin123"
    },
    
	"devices":[
		{
			"device":"RUTX11",
			"connection":"ssh",
			"commands":[
				{
					"command":"AT",
                    "arg":"",
					"ExpectedResults":"OK"
				},
                {
					"command":"AT+GMI",
                    "arg":"",
					"ExpectedResults":"OK"
				},
                
				{
					"command":"ATI",
                    "arg":"",
					"ExpectedResults":"ERROR"
				}
			]
		},
		{
			"device":"TRM240",
			"connection":"serial",
			"commands":[
				{
					
					"command":"AT",
                    "arg":"",
					"ExpectedResults":"OK"
				},
				{
					"command":"ATI",
                    "arg":"", 
					"ExpectedResults":"ERROR"
				},
				{
					"command":"AT+GMM",
                    "arg":"", 
					"ExpectedResults":"ERROR"
				}
			]
		}
	]
}



```

## Usage

Script is started using main.py module with device name and connection parameters as flags. 

Before name you need to write -d or --device to send device name as flag.

Then depending device connection type you are going to send :

For serial: -b baudRate -s serialPort (The order does not matter )

For ssh: -i deviceIP -l connectionUsername -p password -po port (The order does not matter )


#### Example

For ssh connection device:

python3.6 main.py -d RUTX11 -i 192.168.1.1 -l root -p Admin123 -po 22

For serial connection device:

sudo python3.6 main.py -d TRM240 -b 9600 -s /dev/ttyUSB3
