from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '港交所新品'
Mobile = convert(concrete1,task)
atall = False
content_txt = '陈富贵提醒您：请核查港交所新品、分红'
dingTalk(content_txt,Mobile,atall)