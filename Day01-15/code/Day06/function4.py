"""
Python常用模块
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(type(localtime))
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
# strptime： p表示parse，表示分析的意思，所以strptime是给定一个时间字符串和分析模式，返回一个时间对象。
# strftime： f表示format，表示格式化，和strptime正好相反，要求给一个时间对象和输出格式，返回一个时间字符串
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)


shutil.copy('C:/Users/Administrator/Desktop/wordcloud.py', 'C:/Users/Administrator/Desktop/wordcloud1.py')
os.system('ls -l')  # 乱码是因为系统返回的是GBK，而pycharm控制台使用的是UTF-8
os.chdir('C:/Users/Administrator/Desktop/')
os.system('ls -l')
os.mkdir('test')
