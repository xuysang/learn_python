from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = 'ETF申赎'
Mobile1 = convert(concrete1,task)
atall = False
content_txt1 = '陈富贵提醒您：进行ETF嘉实对比'
dingTalk(content_txt1,Mobile1,atall)
