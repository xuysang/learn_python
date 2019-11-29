from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '提取财汇数据'
concrete2 = 'ETF申赎'
Mobile1 = convert(concrete1,task)
Mobile2 = convert(concrete2,task)
atall = False
content_txt1 = '陈富贵提醒您：提取财汇数据'
content_txt2 = '陈富贵提醒您：核查ETF申赎'
dingTalk(content_txt1,Mobile1,atall)
dingTalk(content_txt2,Mobile2,atall)