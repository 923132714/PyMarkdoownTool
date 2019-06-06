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