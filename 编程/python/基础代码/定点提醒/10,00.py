from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '三四级库表专项语句'
Mobile = convert(concrete1,task)
atall = False
content_txt = '陈富贵提醒您该点三四级库表专项语句啦'
dingTalk(content_txt,Mobile,atall)