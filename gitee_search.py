# -*- coding: utf-8 -*-
import os
import sys
import re
import io
import time
import requests
from urllib import parse

def read_exce():
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
	for i in range(m+1):
		i = i+1
		url = 'https://search.gitee.com/?q='+strtext+'&skin=rec&type=repository&pageno='+str(i)
		response = requests.get(url,headers=header)
		
		reurl = re.findall('<a href="(.+?)" class="ns" target="_blank">',response.text)
		rename = re.findall('                                        (.*)</a>',response.text)
		#print (rename)
		
		try:
			if i == m:
				if z==0:
					for n in range(11):
						reurl[n] = reurl[n]
						rename[n] = rename[n].replace('</span>','')
						rename[n] = rename[n].replace('<span class="hl">','')
						print (reurl[n+1],rename[n])
						#print (rename[n])
						continue
				else:
					for n in range(z):
						reurl[n] = reurl[n]
						rename[n] = rename[n].replace('</span>','')
						rename[n] = rename[n].replace('<span class="hl">','')
						print (reurl[n+1],rename[n])
						#print (rename[n])
						continue
			else:
				for n in range(10):
					reurl[n] = reurl[n]
					rename[n] = rename[n].replace('</span>','')
					rename[n] = rename[n].replace('<span class="hl">','')
					print (reurl[n+1],rename[n])
					#print (rename[n])
					continue
		except IndexError:
			pass


if __name__ == '__main__':
	read_exce()