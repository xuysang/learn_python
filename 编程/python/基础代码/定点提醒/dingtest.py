#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author tom
import requests
import json
'''
def dingTalkBBB(content_txt,Mobile,atall):
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
    requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=42eb44f169ab2c9953f78b8ca4aabcf28d7a9216beb52ddd767a521c018e9811',data=json_data,headers=headers)
'''
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




