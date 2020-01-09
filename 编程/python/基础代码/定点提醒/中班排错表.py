from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	

concrete1 = '中班'
Mobile1 = convert(concrete1,task)
atall = False
content_txt1 = '陈富贵提醒您：确认排错表是否有未复核检验数据'
dingTalk(content_txt1,Mobile1,atall)

