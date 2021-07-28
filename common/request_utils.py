# import request
from common.config_utils import ConfigUitls
from common.testdata_utils import TestdataUtils
class Request_Utils():
    def __init__(self):
        config=ConfigUitls()
        self.host=config.HOSTS
        print(self.host)
if __name__=='__main__':
    req=Request_Utils()