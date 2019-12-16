from multiprocessing import Pool
import requests
import json
def f(pagenum):
	get_url = 'https://www.phfund.com.cn/web/fundproducts/getMsNetvalueAndNetvalue?pageInfo.sortField=e.fdate&pageInfo.sortDistanct=desc&pageInfo.currentPage=%s&entity.fundId=1301&entity.isHistory=-1&beginEffectivedate=&endEffectivedate='%pagenum
	headers = {
	    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
	 }
	login_page = requests.get(get_url, headers=headers)
	return json.loads(login_page.text)
if __name__=='__main__':
	with Pool(5) as p:
		print(p.map(f,[x for x in range(1,4)]))


