import requests
import base64
import hashlib
import time
import json


class api_get:
    def __init__(self):
        self.url = "http://tupapi.xfyun.cn/v1/currency"
        self.app_id = "cf893b45"
        self.api_key = "f075ea88c3e99d56a94d8a87a45477d2"

    def get_header(self):
        cur_time = str(int(time.time()))
        param = "{\"image_name\":\"" + "image_name" + "\",\"image_url\":\"" + "\"}"
        param_base64 = base64.b64encode(param.encode('utf-8'))
        tmp = str(param_base64, 'utf-8')

        m2 = hashlib.md5()
        m2.update((self.api_key + cur_time + tmp).encode('utf-8'))
        check_sum = m2.hexdigest()

        header = {
            'X-CurTime': cur_time,
            'X-Param': param_base64,
            'X-Appid': self.app_id,
            'X-CheckSum': check_sum,
        }
        return header

    def get_body(self, file_path):
        with open(file_path, 'rb') as binfile:
            data = binfile.read()
        return data

    def label_get(self, file_path):
        header = self.get_header()
        body = self.get_body(file_path)

        r = requests.post(self.url, headers=header, data=body)
        print(r)
        if r.status_code == 200:
            str_data = r.content.decode("utf-8")
            dict_data = json.loads(str_data)
            print(dict_data)
            label_true = dict_data["data"]["fileList"][0]["label"]
            return label_true
        else:
            return None

