import yaml

class YmlParser(object):

    def __init__(self):
        pass

    def yml_parse(self):
        fd = open('data/config.yml', 'r')
        dic_yml = yaml.load(fd)
        return dic_yml