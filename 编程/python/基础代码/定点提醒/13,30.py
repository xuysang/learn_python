from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '过电子公告'
concrete2 = '核查港交所专项'
Mobile1 = convert(concrete1,task)
Mobile2 = convert(concrete2,task)
atall = False
content_txt1 = '陈富贵提醒您：过电子公告'
content_txt2 = '陈富贵提醒您：核查港交所专项'
dingTalk(content_txt1,Mobile1,atall)
dingTalk(content_txt2,Mobile2,atall)