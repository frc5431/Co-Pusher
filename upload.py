from __future__ import print_function

from zeroconf import zeroconf
from configurations import Config
from logs import Logger

import base64
import paramiko
import os

'''
client = paramiko.SSHClient()
client.load_system_host_keys() #get_host_keys().load(os.path.expanduser("~/.ssh/known_hosts"))
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('localhost', username='', password='')
stdin, stdout, stderr = client.exec_command('ls -l')

print("GOT OUTPUT: %s" % stdout.read())
client.close()
'''

def ping_test(ip_addr):
    param = "-c 1"

    if Config.get_system_type() in "win": 
        param = "-n 1"

    return os.system("ping %s %s" % (param, ip_addr)) 

class Client(object):
    
    def __init__(self):
        self._config = Config()
        self._log = Logger("CLIENT")
        self._log.log("Starting the SSH client")

        self._ip_addr = self._config['robot_ip']
        self._bkp_addr = self._config['backup_ip']
        self._usb_addr = self._config['usb_ip']
        self._username = self._config['robotupload']['username']
        self._password = self._config['robotupload']['password']

    def connect(self):
        self._log.log("Attemtpting to connect to %s" % self._ip_addr)
        if not ping_test(self._ip_addr):
            self._log.logwarn("Failed connecting to: %s" % self._ip_addr)
            self._log.logwarn("Could not find the robot using the default ip! Trying backup ip...")
            if not ping_test(self._bkp_addr):
                self._log.logwarn("Failed connecting to: %s" % self._bkp_addr)
                self._log.logwarn("Could not find the robot using the static backup ip! Trying usb..")
                if not ping_test(self._usb_addr):
                    self._log.logerr("Failed finding robot at usb address! %s" % self._usb_addr)
                    self._log.logerr("Fatal exit! Couldn't find robot")
                    exit(1)
                else:
                    self._log.loggood("Connected to robot via usb! %s" % self._usb_addr)
                    address = self._usb_addr
            else:
                self._loggood("Connected to robot via static backup ip! %s" % self._bkp_addr)
                address = self._bkp_addr
        else:
            self._log.loggood("Connected to robot via mdns! %s" % self._ip_addr)
            address = self._ip_addr

        self._log.log("Starting the ssh client with the robot")


if __name__ == "__main__":
    print("starting")
    logger = Logger()
    logger.logerr("yaaay")

    config = Config()
    print(config['robot_ip'])

    print('\n'.join(zeroconf.ZeroconfServiceTypes.find()))

    #uploader = Client()
    #uploader.connect()
