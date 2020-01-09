from sm_make import *
import os
import time
import requests
import json
import re
import xlsxwriter
import datetime


def mulu_new(date, Project):
    yyyy = re.sub(r'-.*', '', date)
    mm = re.sub(r'^\d+-|-\d+$', '', date)
    dd = re.sub(r'.*-', '', date)
    Project2 = Project + yyyy + '\\' + mm + '\\' + dd + '\\'
    return Project2


Project = '//10.3.2.15//数据二部共享//基金组//四大报数据源下载//证监会公告//'
Project_title = '//10.3.2.15//数据二部共享//基金组//四大报数据源下载//公告标题//'

sm_makes(Project)
today = datetime.datetime.now().strftime("%Y-%m-%d")


url = 'http://eid.csrc.gov.cn/fund/disclose/upload_info_list_page.do?aoData=%5B%7B%22name%22%3A%22sEcho%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22iColumns%22%2C%22value%22%3A6%7D%2C%7B%22name%22%3A%22sColumns%22%2C%22value%22%3A%22%2C%2C%2C%2C%2C%22%7D%2C%7B%22name%22%3A%22iDisplayStart%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22iDisplayLength%22%2C%22value%22%3A20%7D%2C%7B%22name%22%3A%22mDataProp_0%22%2C%22value%22%3A%22fundCode%22%7D%2C%7B%22name%22%3A%22mDataProp_1%22%2C%22value%22%3A%22fundId%22%7D%2C%7B%22name%22%3A%22mDataProp_2%22%2C%22value%22%3A%22organName%22%7D%2C%7B%22name%22%3A%22mDataProp_3%22%2C%22value%22%3A%22reportName%22%7D%2C%7B%22name%22%3A%22mDataProp_4%22%2C%22value%22%3A%22reportSendDate%22%7D%2C%7B%22name%22%3A%22mDataProp_5%22%2C%22value%22%3A%22reportDesp%22%7D%2C%7B%22name%22%3A%22fundCompanyShortName%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22fundCompanyCode%22%7D%2C%7B%22name%22%3A%22fundCode%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22fundShortName%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22fundType%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22reportTypeCode%22%2C%22value%22%3A%22FB030030%22%7D%2C%7B%22name%22%3A%22reportYear%22%2C%22value%22%3A%222019%22%7D%2C%7B%22name%22%3A%22startUploadDate%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22endUploadDate%22%2C%22value%22%3A%22%22%7D%5D&_=1578540158536'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(url, headers=headers)
mydict = json.loads(response.text)
list_01 = mydict['aaData']
for each in list_01:
    reportName = each['reportName']
    uploadInfoId = each['uploadInfoId']
    fundId = each['fundId']
    reportSendDate = each['reportSendDate']
    organName = each['organName']
    url = 'http://eid.csrc.gov.cn/fund/disclose/instance_show_pdf_id.do?instanceid=' + str(uploadInfoId)
    title = str(re.sub('[\/:*?"<>|]', '-', reportName) + ".pdf")
    
    Project_new = mulu_new(today, Project)
    sm_makes(Project_new)
    m = os.listdir(Project_new)
    if title is None or (title in m):
        pass
    else:
        address = Project_new + title
        f = requests.get(url)
        with open(address, "wb") as code:  # 下载文件
            code.write(f.content)
