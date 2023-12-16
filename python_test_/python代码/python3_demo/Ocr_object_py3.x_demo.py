import requests
import time
import hashlib
import base64
#图片数据可以通过两种方式上传，第一种在请求头设置image_url参数，第二种将图片二进制数据写入请求体中。若同时设置，以第一种为准。
#使用二进制数据写入请求体时，不需要在header中传递image_url参数
#使用传递url参数时，请求体为空即可
#本例采用传递图片url的方式
#具体请参考接口文档：https://doc.xfyun.cn/rest_api/
 
URL = "http://tupapi.xfyun.cn/v1/currency"
APPID = "*****"
API_KEY = "***********"
ImageName = "img.jpg"
ImageUrl = "http://hbimg.b0.upaiyun.com/a09289289df694cd6157f997ffa017cc44d4ca9e288fb-OehMYA_fw658"


# FilePath = r"C:\Users\Admin\Desktop\1539656523.png"


def getHeader(image_name, image_url=None):
    curTime = str(int(time.time()))
    param = "{\"image_name\":\"" + image_name + "\",\"image_url\":\"" + image_url + "\"}"
    paramBase64 = base64.b64encode(param.encode('utf-8'))
    tmp = str(paramBase64, 'utf-8')

    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + tmp).encode('utf-8'))
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
    }
    return header


# def getBody(filePath):
#     binfile = open(filePath, 'rb')
#     data = binfile.read()
#     return data


r = requests.post(URL, headers=getHeader(ImageName, ImageUrl))
print(r.content)
