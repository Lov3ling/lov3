# -*- coding: utf-8 -*-
#-*- by:Lee -*-
#-*- date:2017-02-16 -*-
import requests
import json
import time
import re

print("input-username:")					#输入账号
user =input()
print("input-password:")					#输入密码
passwd =input()
print("input-your want search:")			#搜索内容				
search=input()
print("input-your result filename:")		#保存结果的文件
result=input()
print("input-your search pages")			#搜索的页数数量
page=input()
data = {'username': user,'password': passwd}
data_encoded = json.dumps(data)				#json编码
url='https://api.zoomeye.org/user/login'	
a=requests.post(url,data_encoded)
JWT=a.text
token="JWT"+" "+JWT[18:-2]					#获取token并重写
print(token)
txt=open(result,"a+")
r='\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
reg=re.compile(r)

header={"Authorization":token}
for i in range(1,int(page)):
	#query=port:21%20city:beijing&page=1&facets=app,os'
	url='https://api.zoomeye.org/host/search?query='+search+'&page='+str(i)		
	X=requests.get(url,headers=header)
	html=X.text
	a=re.findall(reg,html)
	for i in a:
		txt.write(i+'\n')
		print (i)
	time.sleep(2)
