from xToolkit import xfile
import yaml
import json
class Prser:
    def parserConfig(self):
        path = '/Users/liyang/PycharmProjects/autohttptest/configs/config.yml'
        with open(path) as f :
            config = yaml.safe_load(f)
        print(config)
        env = config[0]['runenv']
        for i in config:
            print(i)
            if env in i.keys():
                return i[env]


    def parserExcel(self,path=''):
        with open(path) as f :
            config = json.safe_load(f)
        return config

    def parserJson(self,path=''):
        with open(path) as f :
            config = json.safe_load(f)
        return config

    def parserYaml(self,path=''):
        path = '/Users/liyang/PycharmProjects/autohttptest/data/baidu.yml'
        with open(path) as f :
            config = yaml.safe_load(f)
        print(config)

    def parserXmid(self,path=''):
        with open(path) as f :
            config = yaml.safe_load(f)
        return config

    def parser_url_keyword(self,path):
        path = '/Users/liyang/PycharmProjects/autohttptest/data/baidu.yml'
        with open(path) as f:
            config = yaml.safe_load(f)
        for i in config:
            # keyword 替换
            pass

    def parser_assert(self,path):
        path = '/Users/liyang/PycharmProjects/autohttptest/data/baidu.yml'
        with open(path) as f:
            config = yaml.safe_load(f)
        for i in config:
            # assert 关键词检测并替换
            # in 包含该关键词
            # not_in 不包含关键字
            # between(1,10)，关键字在1< <10
            pass


if __name__ == '__main__':
    p = Prser()
    c = p.parserConfig()
    print(c)