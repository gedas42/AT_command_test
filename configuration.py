import json
import time

class config:

    __config = None

    def __init__(self, device, config="data.json"):
        self.device = device
        self.filename=config
        self.loadConfig()

    def loadConfig(self):
        config = open(self.filename)
        self.__config = json.load(config)
        time.sleep(1)
        self.__closeConfig__(config)

    def getMailConfig(self):
        return self.__config['mail']


    def getDeviceConfig(self):
        for dev in self.__config["devices"]:
            if dev["device"] == self.device:
                device=dev
        return device


    def __closeConfig__(self,config):
        if self.__config:
            config.close()
