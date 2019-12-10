import requests
def company_name(id):
    url = 'http://www.cninfo.com.cn/new/newInterface/getFundCompany'
    res = requests.get(url).json()
    result = []
    for each in res:
        result += res[each]
    for eachone in result:
        if eachone['companyId']==id:
            return eachone['companyName']

