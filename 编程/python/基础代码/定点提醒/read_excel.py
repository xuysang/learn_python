import xlrd
import time
from dingtest import dingTalk
def read_excel(file= '//10.3.2.15//数据二部共享//基金组//定点业务安排//2020年//定点业务安排.xlsx'):
	wb = xlrd.open_workbook(file)
	# sheet1 = wb.sheet_by_index(0)
	sheet1 = wb.sheet_by_name('Sheet1')
	cols_task = sheet1.col_values(0)
	cols_name1 = sheet1.col_values(3)
	cols_name2 = sheet1.col_values(4)
	i = 2
	task = {}
	for each in cols_task[2:37]:
		list_0 = [cols_name1[i],cols_name2[i]]
		task[each] = list_0
		i+=1
	return task

def convert(concrete,task):
	mobile = {'陈耀威' : '15967192774','陈泽霖' : '18258085694','董婷婷' : '17398308126','方湾湾' : '18058816124','冯佳依' : '18405815424','胡超' : '15967152728','李政远' : '17826827743','李钰莹' : '13654131410','林康' : '15669110721','卢荐' : '17326075068','卢冕' : '15868846226','茅雷成' : '13067783670','任得群' : '15269049997','宋彬' : '18268192106','苏爱' : '15088645474','王永康' : '13173688770','徐晨燕' : '15968172084','徐雨桑' : '15168336099','颜飘' : '18657186418','杨海婷' : '15868875290','张森' : '18895380041','周胜男' : '18757033052','周文兵' : '15384025502'}
	list_0 = task.get(concrete)
	print(list_0)
	list_final = []
	for each in list_0:
		try:
			list_final.append(mobile[each])
		except KeyError as e:
			pass
		
	return list_final
if __name__=='__main__':
	task = read_excel()


'''	
	# file = '定点业务安排（11-25~11-29）.xlsx'
	# task = read_excel(file)
	localtime = time.strftime("%H:%M", time.localtime())

	#concrete1 = '三四级库表专项语句'
	Mobile =["13654131410",]
	atall = False
	content_txt = '提醒：大家好，我要下班了'
	dingTalk(content_txt,Mobile,atall)


	if localtime == '7:00' or localtime == '8:30' or localtime == '10:30' or localtime == '13:30' or localtime == '15:30':
		concrete1 = '过电子公告'
		Mobile = convert(concrete1,task)
		atall = False
		content_txt = '小助手提醒您该过电子公告啦'
		dingTalk(content_txt,Mobile,atall)

'''
'''
content_txt = '呸呸'
Mobile = ["13654131410",]
atall = False
dingTalk(content_txt,Mobile,atall)

#dingTalk('呸呸',["13654131410"],False)

'''

