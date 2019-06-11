# -*- coding: UTF-8 -*-
import frontmatter
import logging
import os

import util
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

        self.__content = self.__post.content
        self.__date =datetime.date.today().strftime('%Y/ %m/ %d')
        self.__get_date()
        self.__get_updated()
    def __get_date (self):
        '''
        获取创作时间（如果有，否则为默认值运行当天）
        :return:
        '''
        if 'date' in self.post.keys():
            self.__date = self.post.__getitem__('date')
        elif 'data' in self.post.keys():
            self.__date = self.post.__getitem__('data')
        else:
            return False
        return True
    def __get_updated (self):
        '''
        获取创作时间（如果有，否则为默认值运行当天）
        :return:
        '''
        if 'update' in self.post.keys():
            self.__updated = self.post.__getitem__('updated')
        elif 'updated' in self.post.keys():
            self.__updated = self.post.__getitem__('updated')
        else:
            return False
        return True
    # def save_as (self,dir,)
    def write_file(self,path = "",post={}):
        '''
        另存为文件
        :param path:
        :return:
        '''
        if path == "":
            path = self.__path
        if post == {}:
            post = self.post
        if self.__date or self.__get_date():
            post.metadata['date']=self.__date
        if self.__updated or self.__get_updated():
            post.metadata['updated']=self.__updated
        with open(path, 'wb+') as f :
            frontmatter.dump(post, f)
    def read_frontmatter(self, path=""):
        '''
        读取front matter成dict，并返回yaml_data
        :param path:
        :return:
        '''
        if path == "":
            path = self.path
        post = frontmatter.load(path)

        return post.metadata

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
        return self.post.metadata
    @metadata.setter
    def metadata(self,data):
        self.post.metadata=data
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date



if __name__ == "__main__":
    file = "E:/WorkSpace/page/my_blog/CSBasics/概率论与数理统计/概率论与数理统计(1).md"
    file = 'test.md'
    md = MdEditor(file)
    logging.basicConfig(level=logging.INFO)
    print(md.metadata)
    print()
    print(md.metadata['html'])
    print()
    # print(md.to_dict())
    print()
    # print(md.metadata.keys())
    print()
    # print(md.remove_yaml())
    print()
    data = {'hhh':'hhhhhh','hahaha':{'kkk':1,'qwqw':True}}
    print(md.post)
    md.metadata=data
    print(md.metadata)
    print()
    date = util.date_to_str( md.date)
    md.write_file(os.getcwd()+"\\"+ date+"-test1.md")


