
import hashlib
import requests
import time
import random
import string
from urllib.parse import quote


class qqGossip(object):
    def __init__(self, question):
        self.app_id = '2121178524'
        self.app_key = 'trT7klex2cvR6dRM'
        self.question = question

    def encryptMD5(self,sign):
        ciper = hashlib.md5(sign.encode('utf-8'))
        return ciper.hexdigest().upper()

    def getParams(self):
        timeStamp = str(int(time.time()))
        nonceStr = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        params = {
            'app_id' : self.app_id,
            'session' : '10000',
            'question' : self.question,
            'time_stamp' : timeStamp,
            'nonce_str' : nonceStr,
        }
        sign = ''
        for key in sorted(params):
            # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
            sign += '{}={}&'.format(key, quote(params[key], safe=''))
        # 将应用密钥以app_key为键名，拼接到字符串sign末尾
        sign += 'app_key={}'.format(self.app_key)
        # 对字符串sign进行MD5运算，得到接口请求签名  
        encryptSign = self.encryptMD5(sign)
        params['sign'] = encryptSign
        return params

    def getGossipAnswer(self):
        url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
        params = self.getParams()
        resBack = requests.post(url,data=params)
        return resBack.json()["data"]["answer"]