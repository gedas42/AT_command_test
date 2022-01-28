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


### Device structure

#### For SSH connection device:

"device": Device name for which the configuration is being created.
"connection": Connection type that this device is using.
"host": Device IP address
"port": Connection port for SSH connection
"login": Username for SSH connection authentification
"password":Password for SSH connection authentification.
"commands":[] All AT commands for the specified device are stored inside commands array.

#### For serial connection device.

#### Command structure

"device":Device name for which the configuration is being created.

"connection":Connection type

"serialPort": Connection port

"baudRate": Baud rate

### Command structure

"command": AT command that will be tested

"param": Parameters for the command if needed, if not write "" with nothing inside.

"expectedOutput": Expected output of the modem command.

## Json example

```json
{
	"devices":[
		{
			"device":"RUTX11",
			"connection":"ssh",
            "host":"192.168.1.1",
            "port":"22",
			"login":"root",
			"password":"Admin123",
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
			"serialPort":"/dev/ttyUSB3",
            "baudRate":"9600",
			"commands":[
				{
					
					"command":"AT",
                    			"arg":"",
					"ExpectedResults":"OK"
				},
				{
					"command":"ATI",
                    			"arg": "+3705457", 
					"ExpectedResults":"ERROR"
				},
				{
					"command":"AT+GMM",
                    			"arg": "", 
					"ExpectedResults":"ERROR"
				}
			]
		}
	]
}

```

## Usage

Script is started using main.py module with device name as parameter. Before name you need to write -p or --product to send device name as flag.

#### Example

For ssh connection device:

python3.6 main.py -p RUTX11 or python main.py --product RUTX11

For serial connection device:

sudo python3.6 main.py -p TRM240 or sudo python3.6 main.py --product TRM240
