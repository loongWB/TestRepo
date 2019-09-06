
from aip import AipOcr
import json

class bdOCR(object):
    def __init__(self, imgURL):
        self.APP_ID = '17079396'
        self.API_KEY = 'qYfeYGjmyLbMX9faHmBCZIkk'
        self.SECRET_KEY = 'BpBeRGWHLtIgrwhbOtQ9jHLK2PWpVYuS'
        self.imgURL = imgURL

    def getOCRResult(self):
        client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        """ 如果有可选参数 """
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "false"

        """ 带参数调用通用文字识别, 图片参数为本地图片 """
        back = client.basicGeneralUrl(self.imgURL, options)
        return back['words_result']
