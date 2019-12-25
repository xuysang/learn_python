from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '货币净值核查'
Mobile = convert(concrete1,task)
atall = False
content_txt = '陈富贵提醒：公开净值表未检验的货币合并值'
dingTalk(content_txt,Mobile,atall)