from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '货币理财节假日净值不一致邮件'
concrete2 = '货币净值核查'
Mobile1 = convert(concrete1,task)
Mobile2 = convert(concrete2,task)
atall = False
content_txt1 = '陈富贵提醒您：请发送货币理财节假日净值不一致邮件'
content_txt2 = '陈富贵提醒您：请跟踪证监会合并值'
dingTalk(content_txt1,Mobile1,atall)
dingTalk(content_txt2,Mobile2,atall)