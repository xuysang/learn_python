from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '跟踪官网'
Mobile1 = convert(concrete1,task)
atall1 = True
content_txt1 = '陈富贵提醒您：该跟踪官网啦'
dingTalk(content_txt1,Mobile1,atall1)



concrete2 = '晨星评级（中班）'
Mobile2 = convert(concrete2,task)
atall2 = False
content_txt2 = '陈富贵提醒您：该处理晨星评级啦'
dingTalk(content_txt2,Mobile2,atall2)