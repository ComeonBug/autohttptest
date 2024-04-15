import requests

class HttpRequest:
    def httpRequest(self,method,path,param,data,header,host):

        res = requests.request(host=host,method=method,path=path,param=param,data=data,header=header);
        return res