# -*- coding: UTF-8 -*-
import frontmatter
import logging
import os
from format_yaml import YamlFormat
import datetime
class MdEditor():
    
    def __init__ (self,path,format_yaml=True):
        '''

        :param path:文件路径
        :param format_yaml: 是否启用格式化frontmatter，默认启用
        '''
        self.__path = path
        if(format_yaml):
            self.format_yaml()
        self.__post = frontmatter.load(path)
        self.__metadata = self.__post.metadata
        self.__content = self.__post.content
        self.__date =datetime.date.today().strftime('%Y/ %m/ %d')
    def __get_date (self):
        '''
        获取创作时间（如果有，否则为默认值运行当天）
        :return:
        '''
        if 'date' in self.post.keys():
            self.__date = self.post.to_dict('date')
        elif 'data' in self.post.keys():
            self.__date = self.post.to_dict('data')
    # def save_as (self,dir,)
    def write_file(self,path = ""):
        '''
        另存为文件
        :param path:
        :return:
        '''
        if path == "":
            path = self.__path
            
        post = self.__post
        with open(path, 'wb+') as f :
            frontmatter.dump(post, f)
    def read_frontmatter(self, path=""):
        '''
        读取front matter成dict，并赋值给self.yaml_data
        :param path:
        :return:
        '''
        if path == "":
            path = self.path
        post = frontmatter.load(path)
        self.yaml_data = post.metadata

        return self.yaml_data

    def format_yaml(self, path=""):
        '''
        调用YamlFormat 格式化frontmatter，避免格式错误
        :param path:
        :return:
        '''
        if path == "":
            path = self.path
        yaml_format = YamlFormat(path)
        if yaml_format.format_yaml() == None:
            raise ValueError("Has no yaml front matter")

    def remove_yaml(self, path=''):
        '''
        删除文件yaml头
        :param path:
        :return:
        '''
        self.post.metadata=None


    def to_dict(self):
        return self.post.to_dict()

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def path (self):
        return self.__path
    @path.setter
    def path(self,path):
        self.__path = path
    @property
    def post (self):
        return self.__post
    @post.setter
    def post(self,post):
        self.__post = post

    @property
    def metadata(self):
        return self.__metadata




if __name__ == "__main__":
    file = "E:/WorkSpace/page/my_blog/CSBasics/概率论与数理统计/概率论与数理统计(1).md"
    file = 'test.md'
    md = MdEditor(file)
    logging.basicConfig(level=logging.INFO)
    print(md.post.to_dict())
    print()
    print(md.post.keys())
    print()
    print(md.remove_yaml())
    print()
    print(md.post.keys())
    print()
    md.write_file(os.getcwd()+"\\test1.md")


