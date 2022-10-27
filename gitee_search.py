# -*- coding: utf-8 -*-
import os
import xlrd
import xlwt
import sys
import re
import io
import time
import requests
from urllib import parse

def read_exce():
    #worksheet = xlrd.open_workbook(u'gitee_search.xls')
    #sheet_names = worksheet.sheet_names()
    f = xlwt.Workbook()
    sheet2 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    sheet2.write(0,0,'仓库URL')
    sheet2.write(0,1,'作者名称')
    sheet2.write(0,2,'项目名称')
    sheet2.write(0,3,'项目描述')
    strname=input("输入搜索内容：")
    strtext = parse.quote(strname)
    url = 'https://search.gitee.com/?q='+strtext+'&skin=rec&type=repository&pageno='
    header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
        }
    response = requests.get(url,headers=header)
    n=0
    #url = 'https://search.gitee.com/?q='+strtext+'&skin=rec&type=repository&pageno='+str(n)
    pageno = re.findall('&skin=rec&type=repository&pageno=(.+?)"',response.text)
    count = re.findall('<b>(.+?)</b>',response.text)
    print ("找到相关仓库约为"+count[0]+"个")
    count = int(count[0])
    m = count//11
    n = 0 
    z = count%11
    c = 1
    if m < 21:
        m = m
    else:
        m = 19
        z = 11
    for i in range(m+1):
        i = i+1
        url = 'https://search.gitee.com/?q='+strtext+'&skin=rec&type=repository&pageno='+str(i)
        response = requests.get(url,headers=header)
        
        reurl = re.findall('<a href="(.+?)" class="ns" target="_blank">',response.text)
        rename = re.findall('                                        (.*)</a>',response.text)
        print (url)
        try:
            if i == (m+1):
                if z==0:
                    for n in range(11):
                        reurl[n] = reurl[n]
                        rename[n] = rename[n].replace('</span>','')
                        rename[n] = rename[n].replace('<span class="hl">','')
                        name = rename[n].split('/')
                        response1 = requests.get(reurl[n+1],headers=header)
                        rejianjie = re.findall(': (.*)</title>',response1.text)
                        sheet2.write(c,0,reurl[n+1])
                        sheet2.write(c,1,name[0])
                        sheet2.write(c,2,name[1])
                        sheet2.write(c,3,rejianjie)
                        #print (reurl[n+1],rename[n])
                        c=c+1
                        continue
                else:
                    for n in range(z):
                        reurl[n] = reurl[n]
                        rename[n] = rename[n].replace('</span>','')
                        rename[n] = rename[n].replace('<span class="hl">','')
                        name = rename[n].split('/')
                        response1 = requests.get(reurl[n+1],headers=header)
                        rejianjie = re.findall(': (.*)</title>',response1.text)
                        sheet2.write(c,0,reurl[n+1])
                        sheet2.write(c,1,name[0])
                        sheet2.write(c,2,name[1])
                        sheet2.write(c,3,rejianjie)
                        #print (reurl[n+1],rename[n])
                        c=c+1
                        continue
            else:
                for n in range(11):
                    reurl[n] = reurl[n]
                    rename[n] = rename[n].replace('</span>','')
                    rename[n] = rename[n].replace('<span class="hl">','')
                    name = rename[n].split('/')
                    response1 = requests.get(reurl[n+1],headers=header)
                    rejianjie = re.findall(': (.*)</title>',response1.text)
                    sheet2.write(c,0,reurl[n+1])
                    sheet2.write(c,1,name[0])
                    sheet2.write(c,2,name[1])
                    sheet2.write(c,3,rejianjie)
                    #print (reurl[n+1],rename[n])
                    #print (name[0])
                    c=c+1
                    continue
        except IndexError:
            pass
    f.save('gitee_search.xls')


if __name__ == '__main__':
    read_exce()