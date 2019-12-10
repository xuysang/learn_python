import sys
sys.path.append("C:/Users/xuys2/Desktop/代码/编程/python/基础代码/定点提醒")
from dingtest import dingTalk
from read_excel import read_excel,convert
import requests, os, re
from bs4 import BeautifulSoup
from sm_make import *
import datetime
import time
from companyid import company_name

task = read_excel() 
concrete1 = '中班'
Mobile = convert(concrete1,task)
atall = False
content_txt = '陈富贵提醒您<巨潮>披露重要公告啦'



Project = '//10.3.2.15//数据二部共享//基金组//四大报数据源下载//巨潮//'
sm_makes(Project)

i=1
while (True):
    start = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    end = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    start_urls = 'http://www.cninfo.com.cn/new/hisAnnouncement/query/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    postdata = {'pageNum': '%s'%i,
            'pageSize': 30,
            'tabName': 'fulltext',
            'column': 'fund',
            'seDate': end +'~'+ end}
    response = requests.post(start_urls, data=postdata, headers=headers)
    announceCount = response.json()["totalAnnouncement"]
    pages = announceCount / 30 + 1
    print("pages:",pages)
    data = response.json()["announcements"]
    for each in data:
        title = str(re.sub('[\/:*?"<>|]', '-', each["announcementTitle"].strip()))
        name = each["secName"]
        timeStamp = each["announcementTime"]/1000
        date = time.strftime("%Y-%m-%d", time.localtime(timeStamp))
        yyyy = re.sub(r'-.*', '', date)
        mm = re.sub(r'^\d+-|-\d+$', '', date)
        dd = re.sub(r'.*-', '', date)
        address = "http://static.cninfo.com.cn/" + str(each["adjunctUrl"])
        id = each['orgId']
        organName = company_name(id)
        print(date + '\n' + title + '\n' + address)
        Project2 = Project + yyyy + '\\' + mm + '\\' + dd + '\\'
        sm_makes(Project2)
        Download_title = organName + name + title + '.pdf'
        print(Download_title)
        print('*' * 40)
        mulu = Project2 + Download_title
        m = os.listdir(Project2)
        if Download_title is None or (Download_title in m):
            print('存在，跳过')
            pass
        else:
            f = requests.get(address)
            with open(mulu, "wb") as code:
                code.write(f.content)
                print('*' * 40)
                f.close()
            if "发售公告" in title or "分红" in title or "收益分配" in title :
                dingTalk(content_txt,Mobile,atall)
    i = i + 1
    print("第%s页"%i)
    if (i > pages):
        break

