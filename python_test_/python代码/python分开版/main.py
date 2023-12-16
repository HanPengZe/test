from ui import Ui_hanzhe
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt
import numpy as np
import requests
import time
import hashlib
import base64
import json
kinds=0
apple=0
banana=0
watermelon=0
kg=0
price=0
URL = "http://tupapi.xfyun.cn/v1/currency"
APPID = "2e469ae4"
API_KEY = "84855f9dda9f162233c862ab13fa7c86"
def getHeader(image_name, image_url=None):
    curTime = str(int(time.time()))
    param = "{\"image_name\":\"" + image_name + "\"}"
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

def getBody(filePath):
    binfile = open(filePath, 'rb')
    data = binfile.read()
    return data
class ui_window(QWidget, Ui_hanzhe):
    def __init__(self, parent=None):
        super(ui_window, self).__init__(parent)
        self.setupUi(self)

        # self.apple.textChanged.connect(self.text_apple)
        # self.banana.textChanged.connect(self.text_banana)
        # self.watermelon.textChanged.connect(self.text_watermelon)
        # self.kg.textChanged.connect(self.text_kg)
        #
        self.recognition.clicked.connect(self.sum_weight)
        # self.recognition.clicked.connect(self.result_text)
        #
        self.choose.clicked.connect(self.choose_photo)
        self.image_path = None
    def apple_write(self):
        text = self.apple.text()
        print(text)
        global apple
        apple = float(text)
        return apple

    def banana_write(self):
        text = self.banana.text()
        print(text)
        global banana
        banana = float(text)
        return banana

    def watermelon_write(self):
        text = self.watermelon.text()
        print(text)
        global watermelon
        watermelon = float(text)
        return watermelon

    def kg_write(self):
        text = self.kg.text()
        print(text)
        global kg
        kg = float(text)
        return kg
    def choose_photo(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Open Image", "~/Pictures",
                                                    "Image Files (*.png *.jpg *.jpeg)")
        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.image_path = image_path
        ImageName = "picture.png"
        r = requests.post(URL, headers=getHeader(ImageName), data=getBody(filePath=image_path))
        # 解析JSON数据
        data = json.loads(r.content)
        data = data['data']['fileList'][0]['label']
        print(data)
        apple_arr = np.array(
            [15504,15938, 16194, 18125, 18765,161, 1152, 1210, 1267, 2160, 2324, 4115, 4629, 4901, 6134, 6385, 11638, 11824, 12087, 13121, 14374,
              18868, 18961, 19083, 19085, 19349, 1729])
        banana_arr = np.array([ 185,6511, 10202, 12999, 16983, 16988185, 5862])
        watermelon_arr = np.array([832])
        global kinds
        if data in apple_arr:
            kinds = "苹果"
        elif data in watermelon_arr:
            kinds = "西瓜"
        elif data in banana_arr:
            kinds = "香蕉"
        else:
            kinds = '识别错误'
        print(kinds)
        self.recognize.setText(kinds)
        # return kinds

    def sum_weight(self):
        self.apple.textChanged.connect(self.apple_write)
        self.banana.textChanged.connect(self.banana_write)
        self.watermelon.textChanged.connect(self.watermelon_write)
        self.kg.textChanged.connect(self.kg_write)
        # print(kinds)
        weight = self.kg_write()
        print(weight)
        global price
        if kinds == "苹果":
            apple1 = self.apple_write()
            price = apple1 * weight

        elif kinds == "香蕉":
            banana1 = self.banana_write()

            price = banana1 * weight

        elif kinds == "西瓜":
            watermelon1 = self.watermelon_write()

            price = watermelon1 * weight
        print(price)
        self.result.setText(str(price))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = ui_window()
    a.show()
    sys.exit(app.exec_())