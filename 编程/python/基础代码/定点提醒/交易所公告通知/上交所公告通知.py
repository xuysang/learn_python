import sys
sys.path.append("C:/Users/xuys2/Desktop/代码/编程/python/基础代码/定点提醒")
from dingtest import dingTalk
from read_excel import read_excel,convert
import os
import requests
from bs4 import  BeautifulSoup
import random
random_str = str(random.random())


Mobile = ['15967192774','15669110721','17826827743']
atall = False
content_txt = '陈富贵提醒您<上交所>上市公告披露回转交易'


i=1
page_size = 30
url_list =["http://www.sse.com.cn/disclosure/announcement/listing/s_index.htm","http://www.sse.com.cn/disclosure/announcement/listing/s_index_1","http://www.sse.com.cn/disclosure/announcement/listing/s_index_2"] 
for url_0 in url_list:
	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
	response=requests.get(url_0,headers=headers)
	soup = BeautifulSoup(response.content, 'lxml')
	div_list = soup.find_all('dd')
	for each in div_list:
		title = each.text+'.html'
		if "上市交易" in title and "基金" in title:
			url = 'http://www.sse.com.cn' + each.a['href']
			response2 = requests.get(url, headers=headers)
			soup2 = BeautifulSoup(response2.content, 'lxml')
			div_list = soup2.find(class_='article-infor').text
			if "回转" in div_list:
				Project = 'D:\\sublime\\光\\test\\公告\\上交所回转\\'
				m = os.listdir(Project)
				if title is None or (title in m):
					pass
				else:
					address = Project + title
					f = requests.get(url)
					with open(address, "wb") as code:  # 下载文件
						code.write(f.content)
                	dingTalk(content_txt,Mobile,atall)


	# announceCount = response.json()["announceCount"]