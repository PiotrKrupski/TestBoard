from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

class RemoteConnect:
    
    def __init__(self,host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.client = None
        self.scp = None
        self.__connect()
    
    def __connect(self):

        self.client = SSHClient()
        #self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.connect(hostname=self.host, 
                            username=self.username, 
                            password=self.password)
        self.scp = SCPClient(self.client.get_transport())
        return self.client
        
    def disconnect(self):
        self.client.close()
        self.scp.close()
    def exec_command(self,command):
        if self.client is None:
            self.client == self.__connect()
        stdin,stdout,stderr = self.client.exec_command(command)
        status = stdout.channel.recv_exit_status()
        if status is 0:
            return stdout.read()
        else:
            return None
                
    def transfer(self,file,remotepath):
        if self.client is None:
            self.client = self.__connect()
        self.scp.put(file,
                        remotepath,
                        recursive=True)


# ssh = RemoteConnect(host="192.168.0.15")
print("test")