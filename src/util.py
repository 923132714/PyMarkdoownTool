"""
@Time  : 2019/6/6 15:12
@author Logic923
@Project : src
@FileName: util.py
@Software: PyCharm
"""
import time

def date_to_str(date):
    '''
    时间格式转换从%Y/ %m/ %d 转换为 %Y-%m-%d
    :param date:
    :return:
    '''

    tempTime = time.strptime(date,'%Y/ %m/ %d')
    resTime = time.strftime('%Y-%m-%d',tempTime)
    return resTime


import re
import os

class FileName():
    def __init__(self,path="",**kv):
        self.filepath=path
        if path!="":
            self.read_filename()
        items = ['prefix','suffix','name','ext','dir']
        for i in items:
            if i in kv.keys():
                self.__dict__[i] = kv[i]
    def read_filename(self,filename = ""):
        '''
        解析路径记录文件夹，前缀，中间名，后缀，扩展名
        :param filename:
        :return:
        '''
        if filename=="":
            filename =  self.filepath
        self.dir = os.path.dirname(filename)
        base_name, self.ext = os.path.splitext(os.path.basename(filename))
        m = re.split(r'-', base_name)
        self.prefix = '-'.join(m[:-1])
        name = m[-1]
        m = re.split(r'\.', name)
        self.suffix = '.'.join(m[1:])
        self.name = m[0]

    # 后缀名判断
    def is_ext_file(self,ext):
        '''
        后缀名判断
        :param fileext:
        :return:
        '''
        if (self.ext == self.ext):
            return True;
        return False;

    @property
    def path(self):
        return self.dir + "\\" + self.prefix + "-" + self.name + "." + self.suffix + self.ext

    @path.setter
    def path(self, path):
        self.read_filename(path)
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name
    @property
    def prefix(self):
        return self.prefix

    @prefix.setter
    def prefix(self, prefix):
        self.prefix = prefix
    @property
    def suffix(self):
        return self.suffix

    @suffix.setter
    def suffix(self, suffix):
        self.suffix = suffix
    @property
    def ext(self):
        return self.ext

    @ext.setter
    def ext(self, ext):
        self.ext = ext
    @property
    def dir(self):
        return self.dir

    @dir.setter
    def dir(self, dir):
         self.dir = dir





if __name__ == '__main__':

    path = 'E:\\WorkSpace\\page\\github_blog\\_posts\\Android\\2019-01-09-game.txt.md'


    a = FileName(path)
    print(a.get_path())