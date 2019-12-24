from bs4 import BeautifulSoup
import requests
import time
import xlsxwriter
from concurrent import futures

start = time.time()
def get_res_performance(k):
    url = 'http://cn.morningstar.com/quickrank/default.aspx'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    data = {
        '__EVENTTARGET': 'ctl00$cphMain$lbPerformance',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '/wEPDwUJNzc4MTU2Nzg3DxYGHgpDdXJyZW50VGFiBQhzbmFwc2hvdB4JU29ydEZpbGVkBQpTdGFyUmF0aW5nHgdTb3J0RGlyBQRERVNDFgJmD2QWAgIDD2QWAmYPZBYYAgEPDxYCHgRUZXh0BRnor4Tnuqfml6XmnJ/vvJoyMDE5LTAzLTMxZGQCAg8PFgQfAwUa5p+l55yL5pyA6L+R5pyI5pyr6K+E57qnPj4eB1Zpc2libGVnZGQCBw8QDxYGHg1EYXRhVGV4dEZpZWxkBQROYW1lHg5EYXRhVmFsdWVGaWVsZAUCSWQeC18hRGF0YUJvdW5kZ2QQFZcBEC0t5Z+66YeR5YWs5Y+4LS0k5a6J5L+h5Z+66YeR566h55CG5pyJ6ZmQ6LSj5Lu75YWs5Y+4HuWuneebiOWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTljJfkv6HnkZ7kuLDln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2a6YGT5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWNmuaXtuWfuumHkeeuoeeQhuaciemZkOWFrOWPuCrmuKTmtbfmsYfph5Hor4HliLjotYTkuqfnrqHnkIbmnInpmZDlhazlj7ge6LSi6YCa5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4Hui0oumAmuivgeWIuOiCoeS7veaciemZkOWFrOWPuCTotKLpgJror4HliLjotYTkuqfnrqHnkIbmnInpmZDlhazlj7ge6ZW/5a6J5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HumVv+WfjuWfuumHkeeuoeeQhuaciemZkOWFrOWPuCzplb/msZ/or4HliLgo5LiK5rW3Kei1hOS6p+euoeeQhuaciemZkOWFrOWPuB7plb/nm5vln7rph5HnrqHnkIbmnInpmZDlhazlj7gk6ZW/5L+h5Z+66YeR566h55CG5pyJ6ZmQ6LSj5Lu75YWs5Y+4JOWIm+mHkeWQiOS/oeWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lpKfmiJDln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5b636YKm5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4J+S4nOaWuemYv+WwlOazleWfuumHkeeuoeeQhuaciemZkOWFrOWPuCrkuJzmlrnmsYfnkIbotYTkuqfnrqHnkIbpppnmuK/mnInpmZDlhazlj7gk5Lic5pa55Z+66YeR566h55CG5pyJ6ZmQ6LSj5Lu75YWs5Y+4HuS4nOaWueivgeWIuOiCoeS7veaciemZkOWFrOWPuCTkuJzmtbfln7rph5HnrqHnkIbmnInpmZDotKPku7vlhazlj7ge5Lic5ZC05Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuS4nOWFtOivgeWIuOiCoeS7veaciemZkOWFrOWPuCTkuJzkuprogZTkuLDmipXotYTnrqHnkIbmnInpmZDlhazlj7gk5pa55q2j5a+M6YKm5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuicguW3ouWfuumHkeeuoeeQhuaciemZkOWFrOWPuCHlr4zlronovr7ln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5a+M5Zu95Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWvjOiNo+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7moLzmnpfln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5bel6ZO255Ge5L+h5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4J+WFieWkp+S/neW+t+S/oeWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lub/lj5Hln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Zu96YO96K+B5Yi46IKh5Lu95pyJ6ZmQ5YWs5Y+4KuWbvea1t+WvjOWFsOWFi+ael+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lm73ph5Hln7rph5HnrqHnkIbmnInpmZDlhazlj7gq5Zu95byA5rOw5a+M5Z+66YeR566h55CG5pyJ6ZmQ6LSj5Lu75YWs5Y+4IeWbveiBlOWuieWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lm73ono3ln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5Zu95a+/5a6J5L+d5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWbveazsOWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTlm73mipXnkZ7pk7bln7rph5HnrqHnkIbmnInpmZDlhazlj7gh5rW35a+M6YCa5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOWQiOeFpuaZuui/nOWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTmgZLnlJ/liY3mtbfln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5oGS55Sf5oqV6LWE566h55CG5pyJ6ZmQ5YWs5Y+4HuaBkui2iuWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTlvJjmr4Xov5zmlrnln7rph5HnrqHnkIbmnInpmZDlhazlj7gk57qi5aGU57qi5Zyf5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOe6ouWcn+WIm+aWsOWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7ms5Plvrfln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2O5a6J5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWNjuWuneWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTljY7lrrjmnKrmnaXln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2O5a+M5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWNjuiejeivgeWIuOiCoeS7veaciemZkOWFrOWPuCTljY7mtqblhYPlpKfln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2O5ZWG5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOWNjuazsOafj+eRnuWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTljY7ms7Dkv53lhbTln7rph5HnrqHnkIbmnInpmZDlhazlj7gw5Y2O5rOw6K+B5Yi477yI5LiK5rW377yJ6LWE5Lqn566h55CG5pyJ6ZmQ5YWs5Y+4HuWNjuazsOivgeWIuOiCoeS7veaciemZkOWFrOWPuB7ljY7ms7DotYTkuqfnrqHnkIbmnInpmZDlhazlj7ge5Y2O5aSP5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOaxh+WuieWfuumHkeeuoeeQhuaciemZkOi0o+S7u+WFrOWPuCTmsYfkuLDmmYvkv6Hln7rph5HnrqHnkIbmnInpmZDlhazlj7gq5rGH5Liw5oqV6LWE5Z+66YeR77yI6aaZ5riv77yJ5pyJ6ZmQ5YWs5Y+4J+axh+a3u+WvjOWfuumHkeeuoeeQhuiCoeS7veaciemZkOWFrOWPuCTmg6DnkIbln7rph5HnrqHnkIbpppnmuK/m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juWPr+eUqBUCAAAUKwMCZ2dkZAIMDw8WBB4IQ3NzQ2xhc3MFBmFjdGl2ZR4EXyFTQgICZGQCDQ8PFgQfCGUfCQICZGQCDg8PFgQfCGUfCQICZGQCDw8PFgQfCGUfCQICZGQCEg8PFgIfAwUEODM5NmRkAhMPDxYEHgtSZWNvcmRjb3VudALMQR4IUGFnZVNpemUCGWRkAhQPEGRkFgFmZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WPwUdY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nJDAFHWN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZyQxBR1jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmckMQUeY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nNSQwBR5jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmc1JDEFHmN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZzUkMQUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQwBRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDEFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkMgUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQzBRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDMFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkMAUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxBRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDIFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkMwUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQ0BRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDUFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkNgUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQ3BRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDgFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkOQUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMAUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMQUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMgUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMwUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNAUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNQUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNgUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNwUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxOAUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxOQUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxOQUYY3RsMDAkY3BoTWFpbiRjYmxMZXZlbCQwBRhjdGwwMCRjcGhNYWluJGNibExldmVsJDEFGGN0bDAwJGNwaE1haW4kY2JsTGV2ZWwkMgUYY3RsMDAkY3BoTWFpbiRjYmxMZXZlbCQzBRhjdGwwMCRjcGhNYWluJGNibExldmVsJDMFK2N0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwwMSRpbWdTb3J0QXJyb3cFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwwMiRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMDMkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDA0JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwwNSRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMDYkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDA3JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwwOCRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMDkkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDEwJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxMSRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTIkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDEzJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxNCRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTUkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDE2JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxNyRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTgkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDE5JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwyMCRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMjEkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDIyJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwyMyRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMjQkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDI1JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwyNiRjaGtGdW5kBRhjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQPPCsACgEIAgFkDKWTJbsc1nnur62WnBxfyZ408MI=',
        '__VIEWSTATEGENERATOR': '302D9840',
        '__EVENTVALIDATION': '/wEW5wECwc/etQ4Cn7zM0gcCoLzM0gcCs7y4qQoCs7y0qQoC7PrGyggC7PrapQEC7PrugAoC7PqC3AICqvnIgwECxeLmmAsC9KaN2QwCj5Cr7gYClp7A2AkCsYfe7QMC4MuErgUC+7Siww8CgsO3rQICnazVwgwCxeKmywYCxeK6pg8CxeLOgQgCxeLiXALF4va3CQLF4oqTAgLF4p7uCgLF4rLJAwLF4sakDALF4tr/BALF4OKECgLF4M6pAQLF4Iq7CwLF4PbfAgKFtqecDQKgmNKlBgKoiqG4AwKpipm4AwLw36HmBALNk4OlBQLDk4ulBQLCk4ulBQKhmNqlBgLJ0p2MBwLI0q2MBwLt+5O5CQKV5c+SCQLs+4e5CQLL0qWMBwLJ0rmMBwLEoeDTCALI0qGMBwLw3+nlBALftpb4AgLnuP3SDwKpiuW4AwKV5aOTCQKgmKKmBgK6oYTTCAKV5cuSCQLnuO3SDwLi+/u5CQKpiqm4AwLI0rGMBwLkuOnSDwKuiqm4AwLt+5u5CQLy36XmBAKgmKqmBgLkuPHSDwLL0p2MBwLnuOHSDwLz36HmBALnuOnSDwLw3+3lBALCk8elBQKU5aOTCQLz3/nlBALNk/ulBQKhmIqmBgK6obDTCALftpr4AgKuiqG4AwLfts74AgLI0p2MBwKhmKKmBgLftuL4AgLCk5OlBQLmuN3SDwKpiqG4AwLnuPnSDwKhmKqmBgLI0qWMBwLI0rmMBwKgmKamBgLJ0qmMBwLJ0pmMBwKuipm4AwLkuN3SDwKjmIqmBgLDk5elBQLCk+elBQKhmI6mBgLL0pmMBwK7oYzTCALi+5u5CQKpioW4AwLmuOXSDwLftpL4AgKU5YeTCQKU5dOSCQLDk5OlBQLFoYzTCALz3/3lBALFoYDTCAKuirm4AwK6oezTCALnuPXSDwLw3/nlBAKpirm4AwLmuNnSDwLkuO3SDwLFobjTCALetuL4AgKU5aeTCQLI0r2MBwLw3/XlBAKU5deSCQLEoajTCALets74AgLt+5+5CQLw36XmBAKhmK6mBgKmmKqmBgLZts74AgLFoeDTCALFoYTTCAK6obTTCALt+/+5CQLs+4O5CQLJ0r2MBwKoipm4AwLetub4AgKoiuW4AwKU5duSCQLI0qmMBwKuirW4AwKV5YeTCQLCk5ulBQLJ0rGMBwKuir24AwKU5YOTCQKX5YeTCQKjmNalBgLetsL4AgLnuN3SDwLw3/3lBALZtsL4AgKpir24AwLs+/+5CQLCk5+lBQKU5c+SCQKgmI6mBgLz36XmBALy36HmBALi+/+5CQLFobDTCALDk+elBQKV5YOTCQLi+4+5CQLnuPHSDwLi+4u5CQKgmIqmBgLw38HlBALi+5e5CQLz38XlBAKhmNKlBgLkuNnSDwKjmI6mBgLt+/u5CQLkuPXSDwKpirG4AwK6obzTCALNk8elBQLx38HlBAKEiMLTDAKEiMLTDAKQ18zyAwKQ18zyAwLF7Je2DgKvw/+HAQKWjpmUAwLdt+TKBQL10KDSBgL+xcmpAQKIv62ECAKe2tCSDwLF05trAvX32OQPAtTm4bgNAv/S5cQBAtj00aMGAtrrjewDArmenJAPAqGm8ogMAsrQmI0DAsrQ9PACAsrQkEkCytCMKwLK0KiVAgLK0MT3AQLK0OD4DwLK0NzSDwLd3MDRAQLd3LyzAQLd3JiNAwLd3PTwAgLd3JBJAt3cjCsC3dyolQIC3dzE9wEC3dzg+A8C3dzc0g8C3OTA0QEC3OS8swEC3OSYjQMC3OT08AIC3OSQSQLc5IwrAtzkqJUCAvv2wKwBAvWZlsENw6pS2VwYT3nkyxOUpzD3AzzOdu4='

    }
    resp = requests.post(url, headers=headers, data=data)
    soup = BeautifulSoup(resp.content, 'lxml')
    global viewstate
    global eventvalidation
    viewstate = soup.find(id='__VIEWSTATE')['value']
    eventvalidation = soup.find(id='__EVENTVALIDATION')['value']

    data1 = {
        '__EVENTTARGET': 'ctl00$cphMain$AspNetPager1',
        '__EVENTARGUMENT': '%s' %k,
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': '302D9840',
        '__EVENTVALIDATION': eventvalidation
    }
    while True:
        try:
            resp1 = requests.post(url, headers=headers, data=data1)
            break
        except ConnectionError:
            pass
    return (resp1, k)

def get_res(k):
    print(k)
    url = 'http://cn.morningstar.com/quickrank/default.aspx'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.content, 'lxml')
    global viewstate
    global eventvalidation

    viewstate = soup.find(id='__VIEWSTATE')['value']
    eventvalidation = soup.find(id='__EVENTVALIDATION')['value']

    data = {
        '__EVENTTARGET': 'ctl00$cphMain$AspNetPager1',
        '__EVENTARGUMENT': '%s' % k,
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': '302D9840',
        '__EVENTVALIDATION': eventvalidation
    }
    while True:
        try:
            resp1 = requests.post(url, headers=headers, data=data)
            break
        except ConnectionError:
            pass
    return (resp1,k)



def thread_way():
    workers = 10
    with futures.ThreadPoolExecutor(workers) as executor:
        to_do = []
        to_do2 = []
        for i in range(1,374):
            print("正在抓取第%s页" % i)
            future1 = executor.submit(get_res, i)
            future2 = executor.submit(get_res_performance, i)
            to_do.append(future1)
            to_do2.append(future2)
    results1 = []
    results2 =[]
    for future in futures.as_completed(to_do):
        res = future.result()
        results1.append(res)
    for future in futures.as_completed(to_do2):
        res = future.result()
        results2.append(res)
    return (results1,results2)

def write_execl(res1,res2):
    workbook = xlsxwriter.Workbook('晨星评级.xlsx')
    worksheet1 = workbook.add_worksheet('快照')
    worksheet1.write(0, 0, '序号')
    worksheet1.write(0, 1, '代码')
    worksheet1.write(0, 2, '基金名称')
    worksheet1.write(0, 3, '基金分类')
    worksheet1.write(0, 4, '三年')
    worksheet1.write(0, 5, '五年')
    worksheet1.write(0, 6, '净值日期')
    worksheet1.write(0, 7, '单位净值')
    worksheet1.write(0, 8, '净值日变动')
    worksheet1.write(0, 9, '今年以来回报')
    row = 1
    for each in list(res1):
        soup1 = BeautifulSoup(each.content, 'lxml')
        div_list = soup1.find(id="ctl00_cphMain_gridResult")
        div_list1 = div_list.find_all('tr')
        for each1 in div_list1[1:]:
            col = 0
            div_list0 = each1.find_all('td')
            # import pdb
            # pdb.set_trace()
            for y in div_list0[2:]:
                col += 1
                worksheet1.write(row, 0, row)
                if y.text != '':
                    worksheet1.write(row, col, y.text.strip())
                else:
                    try:
                        worksheet1.write(row, col, y.img.attrs['src'])
                        # star_url = y.img.attrs['src']
                        # worksheet.write(row, col, get_captcha(star_url))
                    except AttributeError:
                        worksheet1.write(row, col, '-')
            row += 1

    worksheet = workbook.add_worksheet('业绩和风险')
    worksheet.write(0, 0, '序号')
    worksheet.write(0, 1, '代码')
    worksheet.write(0, 2, '基金名称')
    worksheet.write(0, 3, '1天回报(%)')
    worksheet.write(0, 4, '1周回报(%)')
    worksheet.write(0, 5, '1个月回报(%)')
    worksheet.write(0, 6, '3个月回报(%)')
    worksheet.write(0, 7, '6个月回报(%)')
    worksheet.write(0, 8, '1年回报(%)')
    worksheet.write(0, 9, '2年年化回报(%)')
    worksheet.write(0, 10, '3年年化回报(%)')
    worksheet.write(0, 11, '5年年化回报(%)')
    worksheet.write(0, 12, '10年年化回报(%)')
    worksheet.write(0, 13, '设立以来总回报(%)')
    worksheet.write(0, 14, '三年标准差(%)')
    worksheet.write(0, 15, '三年晨星风险系数')
    row = 1
    for each in res2:
        soup1 = BeautifulSoup(each.content, 'lxml')
        div_list = soup1.find(id="ctl00_cphMain_gridResult")
        div_list1 = div_list.find_all('tr')
        for each in div_list1[1:]:
            col = 0
            div_list0 = each.find_all('td')
            # import pdb
            # pdb.set_trace()
            for y in div_list0[2:]:
                col += 1
                worksheet.write(row, 0, row)
                worksheet.write(row, col, y.text.strip())
            row += 1
    workbook.close()
if __name__=='__main__':
    # freeze_support()
    '''
    res = thread_way()
    res1 = [x[0] for x in res[0]]
    res2 = [x[0] for x in res[1]]
    write_execl(res1, res2)
    '''
    res = thread_way()
    res[0].sort(key=lambda k: k[1])
    res1 = [x[0] for x in res[0]]
    res[1].sort(key=lambda k: k[1])
    res2 = [x[0] for x in res[1]]
    write_execl(res1,res2)


    end = time.time()
    print("时间为", end - start)
