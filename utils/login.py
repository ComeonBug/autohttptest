import requests
from utils.httpRequst import HttpRequest
from utils.parser import Prser
# 登陆，获取token，并写入token.txt文件中
class Login:
    def login(self,username,password,host):
        param = {
            'username': username,
            'password': password
        }
        res = HttpRequest.httpRequest(param=param,method='post',host=host,path='/login')
        self.write_token()


    def write_token(self,res):
        path = '/Users/liyang/PycharmProjects/autohttptest/configs/token.txt'
        with open(path) as f :
            f.write(res.json()['token'])


if __name__ == '__main__':
    pass

