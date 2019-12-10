import sys
sys.path.append("C:/Users/xuys2/Desktop/代码/编程/python/基础代码/定点提醒")
from dingtest import dingTalk
from read_excel import read_excel,convert
import os
import requests
import re
from bs4 import BeautifulSoup
import random

Mobile = ['15967192774','15669110721','17826827743']
atall = False
content_txt = '陈富贵提醒您<深交所>上市公告披露回转交易'


random_str = str(random.random())
request_url = "http://www.szse.cn/disclosure/notice/fund/index.html"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(request_url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
div_list = soup.find(class_='g-conbox')
div_list2 = soup.find_all(class_='title')
for each in div_list2[2:]:
    title_0 = re.findall(r'var curTitle = \'.*?\'', str(each))[0]
    title = title_0.split()[-1].strip(" ' ") + '.html'
    url_0 = re.findall(r'var curHref = \'.*?\'', str(each))[0]
    url = url_0.split()[-1].strip(" ' ")
    url_f = 'http://www.szse.cn/disclosure/notice/fund' + url.replace('.', '', 1)
    response2 = requests.get(url_f, headers=headers)
    soup2 = BeautifulSoup(response2.content, 'lxml')
    div_list = soup2.find(class_='des-content').text
    if "回转" in div_list:
        Project = 'D:\\sublime\\光\\test\\公告\\回转\\'
        m = os.listdir(Project)
        if title is None or (title in m):
            pass
        else:
            address = Project + title
            f = requests.get(url_f)
            with open(address, "wb") as code:  # 下载文件
                code.write(f.content)
            dingTalk(content_txt,Mobile,atall)
'''
for i in range(1,71):
    request_url = "http://www.szse.cn/disclosure/notice/fund/index_%s.html"% i
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    response=requests.get(request_url,headers=headers)
    soup = BeautifulSoup(response.content,'lxml')
    div_list = soup.find(class_='g-conbox')
    div_list2 = soup.find_all(class_='title')
    for each in div_list2[2:]:
        title_0 = re.findall(r'var curTitle = \'.*?\'' ,str(each))[0]
        title = title_0.split()[-1].strip(" ' ")+'.html'
        url_0 = re.findall(r'var curHref = \'.*?\'' ,str(each))[0]
        url = url_0.split()[-1].strip(" ' ")
        url_f = 'http://www.szse.cn/disclosure/notice/fund'+url.replace('.','',1)
        response2 = requests.get(url_f, headers=headers)
        soup2 = BeautifulSoup(response2.content, 'lxml')
        div_list = soup2.find(class_='des-content').text
        if "回转" in div_list:
            Project = 'D:\\sublime\\光\\test\\公告\\回转\\'
            m = os.listdir(Project)
            if title is None or (title in m):
                pass
            else:
                address = Project + title
                f = requests.get(url_f)
                with open(address, "wb") as code:  # 下载文件
                    code.write(f.content)
'''

'''
    announceCount = response.json()["announceCount"]
    pages = announceCount / 30 + 1
    data = response.json()["data"]
    url_01 = "http://disc.static.szse.cn/download"
    for each in data:
        attachPath = each["attachPath"]
        title_01 = each["title"]
        date_str = each["publishTime"][:11]
        pdf_url = url_01 + attachPath
        title = date_str + title_01 + ".pdf"
        Project = '//10.3.2.15//数据二部共享//基金组//四大报数据源下载//交易所公告//'
        m = os.listdir(Project)
        if title is None or (title in m):
            pass
        else:
            address = Project + title
            f = requests.get(pdf_url)
            with open(address, "wb") as code2:  # 下载文件
                code2.write(f.content)
    i = i + 1
    if (i > pages):
        break


'''
