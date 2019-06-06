# -*- coding: UTF-8 -*-
import frontmatter
import re # 正则表达式
import logging

class YamlFormat(object):

    def __init__(self, path = ""):
        self.path = path
    
    def format_colon(self,line):
        # 冒号前后保持空格
        '''
            pattern : 正则中的模式字符串。
            repl : 替换的字符串，也可为一个函数。
            string : 要被查找替换的原始字符串。
            count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

        '''
        pattern = "[ ]*[:][ ]*"
        repl =  " : "
        string = line
        line = re.sub(pattern, repl, string, count=0, flags=0)
        return line
    def format_minus(self,line):
        # 行首减号后保持空格
        '''
            pattern : 正则中的模式字符串。
            repl : 替换的字符串，也可为一个函数。
            string : 要被查找替换的原始字符串。
            count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

        '''
        pattern = "[-][ ]*"
        repl =  "- "
        string = line
        line = re.sub(pattern, repl, string, count=0, flags=0)
        return line
    
    def format_indent(self ,line , last_indent , flag):
        '''
        如果冒号后有信息
            缩进保持
        如果冒号后无信息
            缩进增加
        '''
        num = re.match(r"^ *",line).span()
        indent = num[1]
        
        newflag  = re.search(r":[ ]*[\S]+", line) != None
        logging.debug("format_indent : flag =  %s  ,  indent = %s  , last_indent = %s  "%(flag,indent,last_indent))
        if flag :
            if indent == last_indent:
                return line,last_indent,newflag
            elif indent > last_indent:
                pass
            else:
                last_indent = indent//2*2
        else:
            if indent == last_indent+2:
                last_indent = last_indent+2
                return line,last_indent,newflag
            elif indent <= last_indent:
                last_indent = indent//2*2
            else:
                last_indent  = indent +2
        line = line.strip()
        line = " " * last_indent + line 
        return line,last_indent,newflag
    
    def  read_yaml (self,coding ="utf-8"):
        '''
        自制按行读取front matter 到数组
        '''
        path = self.path
        with open(path,'r+',encoding = coding) as f:
            temp = f.readline()
            if(temp.rstrip() == "---"):
                yaml_list = []
                temp = ""
                # 读取 front matter
                while(temp.rstrip() != "---"):
                    temp = f.readline()
                    
                    if temp == None:
                        # no complete front matter
                        return None
                    
                    yaml_list.append( temp.rstrip())
                yaml_list.pop(-1)
                self.yaml_list = yaml_list
                

                # 读取 文档内容
                self.content = f.read()
                logging.info("read_yaml :  content : \n %s" % self.content)
                
                return yaml_list
            return None
    def save_yaml(self,coding = "utf-8"):
        '''
        自制从数组存到文件，会覆盖！慎用
        '''
        path = self.path
        if self.content == None or self.content =="" :
            logging.warn("write null string content !!!")
            raise Exception("save null string content")
        buffer = "---\n"
        for item in self.yaml_list:
            buffer += item +"\n"
        buffer += "---\n"
        logging.info("save_yaml : buffer :\n %s" %buffer)
        with open(self.path,'w+',encoding = coding) as f:
            f.write(buffer)
            f.write(self.content)
        
    def format_yaml(self):
        '''
        规范化 front matter
        '''
        logging.info("yaml\n---")
        last_indent = 0
        flag = True
        path = self.path

        if self.read_yaml() == None:
            return None

        yaml_list =self.yaml_list
        if yaml_list == None:
            return None
        for i in range(0,len(yaml_list)):
            item = yaml_list[i]
            # 空行
            if item == '': continue
            # 注释
            if  re.match(r"^ *#", item) != None :
                continue
            
            logging.info(item)
            # 冒号格式化
            
            item =self.format_colon(item)
            # 减号格式化
            item = self.format_minus(item)
            # 缩进格式化 
            item,last_indent,flag  = self.format_indent(item,last_indent,flag)
            print(item)
            yaml_list[i] = item
        logging.info("---")
        self.yaml_list =yaml_list
        self.save_yaml()
        return yaml_list
  
        

       
        
    @property
    def path(self):
        return self.__path
    @path.setter
    def path(self,path):
        self.__path =  path
    @property
    def yaml_list(self):
        return self.__yaml_list
    @yaml_list.setter
    def yaml_list(self,yaml_list):
        self.__yaml_list = yaml_list
        
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self,content):
        self.__content = content

#
# if __name__ == "__main__":
#     path = "test.md"
#     reader = YamlReader(path)
#     logging.basicConfig(level=logging.DEBUG)
#     reader.format_yaml()
#     data = reader.read_frontmatter()
#     print(data['data'])
#     import util
#
#     date = util.date_to_str(data['data'])
#     print(date)