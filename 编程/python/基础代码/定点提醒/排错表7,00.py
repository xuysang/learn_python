from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	

concrete1 = '排错表'
concrete2 = '排错表复核'
Mobile1 = convert(concrete1,task)
Mobile2 = convert(concrete2,task)
atall = False
content_txt1 = '陈富贵提醒您：确认排错表是否有未复核检验数据'
content_txt2 = '陈富贵提醒您：确认排错表是否已复核'
dingTalk(content_txt1,Mobile1,atall)
dingTalk(content_txt2,Mobile2,atall)
