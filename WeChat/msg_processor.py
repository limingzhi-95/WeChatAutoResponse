#coding=utf8
import itchat
import time
import json
import requests


class TuRingApi(object):
    class MsgType(object):
        Text = 0
        Picture = 1
        Recording = 2

    def __init__(self, api_key, user_id):
        self.api_key = api_key
        self.user_id = user_id

    def send_msg(self, msg_info, msg_type):
        data = {
            "reqType": msg_type,
            "perception": {
                "inputText": {
                    "text": msg_info.get('text', '')
                },
                # "inputImage": {
                #     "url": msg_info.get('img_url', '')
                # },
                # "selfInfo": {
                #     "location": {
                #         "city": msg_info.get('city', ''),
                #         "province": msg_info.get('province'),
                #     }
                # }
            },
            "userInfo": {
                "apiKey": self.api_key,
                "userId": self.user_id
            }
        }
        res = requests.post(url="http://openapi.tuling123.com/openapi/api/v2", json=json.dumps(data), headers={"Content-Type": "application/json"})
        if res.status_code == 200 and res.text['intent']["code"] == 1005:
            return res.text['values', {}].get('text')
        return ""
