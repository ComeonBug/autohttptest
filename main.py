import pytest
from utils import login
from utils import parser

if __name__ == '__main__':
    # 获取对应的用户名密码
    username,password,host = parser.Prser.parserConfig()

    # login 并抓去token，写入token文件
    login.Login(username,password,host)

    # 执行pytest
    pytest.main(['-vs','--capture=sys','-m P0'])
