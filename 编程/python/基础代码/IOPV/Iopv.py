


url = http://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.3723049134781662&marketId=1&code=159919




with open('code.txt','r') as file:
    for line in file:
        code=line.replace('\n','')
        code_list.append(code)