#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author tom
import requests
import json

def dingTalk(content_txt,Mobile,atall):
    headers={
        "Content-Type": "application/json"
            }

    data={"msgtype": "text",
            "text": {
                 "content": content_txt},
            "at":{
                "atMobiles": Mobile,
                "isAtAll": atall
                }
                }      
    json_data=json.dumps(data)
    requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=b879ef41ae666b98bf3744b960e5dedb96d000148558f0de160fa6f8708862bc',data=json_data,headers=headers)




  

'''
    data2 = {
     "msgtype": "markdown",
     "markdown": {
         "title":"杭州天气",
         "text": "#### 杭州天气提醒 @13654131410\n" +
                 "> 9度，西北风1级，空气良89，相对温度73%\n\n" +
                 "> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n"  +
                 "> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n"
     },
    "at": {
        "atMobiles": [
            "13654131410", 
        ], 
        "isAtAll": False
 	}}
 '''