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

concrete3 = '三四级库表专项语句'
Mobile3 = convert(concrete3,task)
atall3 = False
content_txt3 = '陈富贵提醒您该点三四级库表专项语句啦'
dingTalk(content_txt3,Mobile3,atall3)

'''
Mobile3 = ["15088645474","15269049997",]
atall3 = False
content_txt3 = '陈富贵提醒您：到点修改最低限额啦'
dingTalk(content_txt3,Mobile3,atall3)
'''
