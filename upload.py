from __future__ import print_function
import base64
import paramiko
import os

client = paramiko.SSHClient()
client.load_system_host_keys() #get_host_keys().load(os.path.expanduser("~/.ssh/known_hosts"))
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('localhost', username='', password='')
stdin, stdout, stderr = client.exec_command('ls -l')

print("GOT OUTPUT: %s" % stdout.read())
client.close()
