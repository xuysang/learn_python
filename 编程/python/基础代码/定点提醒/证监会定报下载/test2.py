import requests
from bs4 import BeautifulSoup

def get_name(id):
	start_urls = 'http://eid.csrc.gov.cn/fund/disclose/fund_detail.do?fundId=%s'%id
	headers = {
    	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
	response = requests.get(start_urls, headers=headers)
	soup = BeautifulSoup(response.text,'lxml')
	div_list = soup.find(class_='Contentbox')

	return(div_list.text.strip().split()[1])
