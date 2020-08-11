# -*- coding: utf-8 -*-  

# intro: 自动将Markdown文件中的三级标题提取出来，输出对应的html-id，自动滤除标题中的套娃链接
# author: 顾晓 https://github.com/chenyanzz


import re

f = open(input('File name: '),'r',encoding='UTF-8')

for line in f.readlines(100000000):
    if line.startswith('#'):
        line = re.sub('\[(.+?)\]\(.+?\)','\\1',line,100) # 去除标题内的链接格式
        # print(line)
        line = line.replace('#','').strip()
        id=''
        for c in line:
            if c.isalpha(): id+=c.lower()
            if c.isdigit(): id+=c
            if c in (' '): id+='-'
        print(line+'  ->\n  #'+id+)