import configparser
import os

currentfilepath=os.path.dirname(__file__)
configpath=os.path.join(currentfilepath,'..','conf','config.ini')
class ConfigUitls():
    def __init__(self,cof_file_path=configpath):
        self.configparser=configparser.ConfigParser()
        self.configparser.read(cof_file_path)
    @property
    def HOSTS(self):
        hosts=self.configparser.get('default','url')
        return hosts
configread=ConfigUitls()
if __name__=='__main__':
    print(configread.HOSTS)

