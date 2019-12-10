import requests
from bs4 import BeautifulSoup
import re
import os
import time
import sys

def sm_makes(Project):
    if os.path.exists(Project) is False:
        os.makedirs(Project)
        print('创建目录：' + Project)
    else:
        print('下载目录已存在')
    print('开始读取网页信息')
    return Project

def sm_Download(Download_title,Project,address):
    m = os.listdir(Project)
    if Download_title in m:
        print('存在')
        pass
    else:
        print('开始下载')
        mulu = Project + Download_title
        f = requests.get(address)
        # 下载文件
        with open(mulu, "wb") as code:
            code.write(f.content)
            return sm_Download

def sm_Download_headers(Download_title,Project,address,headers):
    m = os.listdir(Project)
    if Download_title in m:
        print('存在')
        pass
    else:
        print('开始下载')
        mulu = Project + Download_title
        f = requests.get(address,headers=headers)
        # 下载文件
        with open(mulu, "wb") as code:
            code.write(f.content)
            f.close()
            return

def sm_xuchuan_download(url, Project,Download_title):
    m = os.listdir(Project)
    if Download_title in m:
        print('文件已存在，跳过')
        pass
    else:
        file_path = Project + Download_title

        r1 = requests.get(url, stream=True, verify=False)

        total_size = int(r1.headers['Content-Length'])
        print( total_size )
        # # 这重要了，先看看本地文件下载了多少
        if os.path.exists(file_path):
            temp_size = os.path.getsize(file_path)  # 本地已经下载的文件大小
        else:
            temp_size = 0
        # 显示一下下载了多少
        # print(temp_size)
        # print(total_size)
        # 核心部分，这个是请求下载时，从本地文件已经下载过的后面下载
        headers = {'Range': 'bytes=%d-' % temp_size,
                   'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
                   }
        # 重新请求网址，加入新的请求头的
        r = requests.get(url, stream=True, verify=False, headers=headers)

        # 下面写入文件也要注意，看到"ab"了吗？
        # "ab"表示追加形式写入文件
        with open(file_path, "ab") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    temp_size += len(chunk)
                    f.write(chunk)
                    f.flush()

        f.close()

def xiecheng(address,mulu):
    f = requests.get(address, headers=headers)
    with open(mulu, "wb") as code:
        code.write(f.content)
        print('*'*40)
        f.close()

def BTgeshihua(title):
    title_gai= re.sub(r'\*|<|>|\?|:|"|\||\\|/|[\s]','',title)
    return title_gai
if __name__ == '__main__':
    print(BTgeshihua( '''[`~!@#$%^&*()_\+=<>?:"{}|,\/;'\\[\]·~！@#￥%……&*（）——\-+={}|《》？：“”【】、；‘'，。、]'''))

