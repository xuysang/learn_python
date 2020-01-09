from test2 import get_name
from sm_make import *
import os
import time
import requests
import json
import re
import time
from concurrent import futures
project = 'E:\\年报公告\\2020\\'
start = time.time()

def complete(each):
    reportName = each['reportName']
    uploadInfoId = each['uploadInfoId']
    fundId = each['fundId']
    reportSendDate = each['reportSendDate']
    organName = each['organName']
    url = 'http://eid.csrc.gov.cn/fund/disclose/instance_show_pdf_id.do?instanceid=' + str(uploadInfoId)
    name = get_name(fundId)
    title = name + '2019年第3季度报告' + ".pdf"
    print(title)
    Project2 = project + reportSendDate + '\\' + organName + '\\'
    sm_makes(Project2)
    m = os.listdir(Project2)
    if title is None or (title in m):
        pass
    else:
        address = Project2 + title
        f = requests.get(url)
        with open(address, "wb") as code:  # 下载文件
            code.write(f.content)

url = 'http://eid.csrc.gov.cn/fund/disclose/upload_info_list_page.do?aoData=%5B%7B%22name%22%3A%22sEcho%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22iColumns%22%2C%22value%22%3A6%7D%2C%7B%22name%22%3A%22sColumns%22%2C%22value%22%3A%22%2C%2C%2C%2C%2C%22%7D%2C%7B%22name%22%3A%22iDisplayStart%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22iDisplayLength%22%2C%22value%22%3A5000%7D%2C%7B%22name%22%3A%22mDataProp_0%22%2C%22value%22%3A%22fundCode%22%7D%2C%7B%22name%22%3A%22mDataProp_1%22%2C%22value%22%3A%22fundId%22%7D%2C%7B%22name%22%3A%22mDataProp_2%22%2C%22value%22%3A%22organName%22%7D%2C%7B%22name%22%3A%22mDataProp_3%22%2C%22value%22%3A%22reportName%22%7D%2C%7B%22name%22%3A%22mDataProp_4%22%2C%22value%22%3A%22reportSendDate%22%7D%2C%7B%22name%22%3A%22mDataProp_5%22%2C%22value%22%3A%22reportDesp%22%7D%2C%7B%22name%22%3A%22fundCompanyShortName%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22fundCompanyCode%22%7D%2C%7B%22name%22%3A%22fundCode%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22fundShortName%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22fundType%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22reportTypeCode%22%2C%22value%22%3A%22FB030030%22%7D%2C%7B%22name%22%3A%22reportYear%22%2C%22value%22%3A%222019%22%7D%2C%7B%22name%22%3A%22startUploadDate%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22endUploadDate%22%2C%22value%22%3A%22%22%7D%5D&_=1578540158536'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(url, headers=headers)
mydict = json.loads(response.text)
list_01 = mydict['aaData']

workers = 4
with futures.ThreadPoolExecutor(workers) as executor:
    res = executor.map(complete, (x for x in list_01))
end = time.time()
print("时间为%.2f分钟"%(float(end - start)/60))
print("已完成")