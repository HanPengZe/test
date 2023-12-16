import requests
import time
import hashlib
import base64
#ͼƬ���ݿ���ͨ�����ַ�ʽ�ϴ�����һ��������ͷ����image_url�������ڶ��ֽ�ͼƬ����������д���������С���ͬʱ���ã��Ե�һ��Ϊ׼��
#ʹ�ö���������д��������ʱ������Ҫ��header�д���image_url����
#ʹ�ô���url����ʱ��������Ϊ�ռ���
#�������ô���ͼƬurl�ķ�ʽ
#������ο��ӿ��ĵ���https://doc.xfyun.cn/rest_api/
 
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
