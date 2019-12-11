import requests
import json
import xlsxwriter


def IOPV(code):
    url = 'http://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.3723049134781662&marketId=1&code=%s'%(code)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }
    login_page = requests.get(url, headers=headers)
    mydict = json.loads(login_page.text)
    try:
        iopv_value = mydict['data']['netValue']
        return iopv_value
    except KeyError:
        pass


code_list=[]
with open('code.txt','r') as file:
    for line in file:
        code=line.replace('\n','')
        code_list.append(code)

row = 0
col = 0
workbook = xlsxwriter.Workbook('iopv.xlsx')
worksheet = workbook.add_worksheet()
for eachone in code_list:
    worksheet.write(row, col, eachone)
    worksheet.write(row, col + 1, IOPV(eachone))
    row += 1
workbook.close()
