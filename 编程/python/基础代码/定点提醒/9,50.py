from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '晨星评级（早班）'
Mobile = convert(concrete1,task)
atall = False
content_txt = '陈富贵提醒您：该处理晨星评级啦'
dingTalk(content_txt,Mobile,atall)