import json
class GetJson():
    @staticmethod
    def getJson(string,parmeter):
        cell_dict = json.loads(string)
        print(cell_dict[parmeter])
