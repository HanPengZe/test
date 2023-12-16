import sys
from PIL import ImageQt, Image
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit,QTextEdit,QFileDialog
from PyQt5.QtGui import QPixmap , QImage
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5 import QtWidgets,QtCore
import requests
import time
import hashlib
import base64
import json
import numpy as np
import pandas as pd
result=0
apple=0
banana=0
xigua=0
kg=0
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

class FruitRecognitionSystem(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.initUI(self)

    def initUI(self,MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("wkWgt")  # 替换背景图片只对当前窗口生效 核心代码
        self.centralwidget.setStyleSheet("#wkWgt{border-image:url(./img.jpg);}")  # 替换图片路径  核心代码
        # 苹果单价
        self.k1 = QLabel(self)
        self.k1.setGeometry(30, 20, 100, 20)
        self.k1.setText('苹果/元：')
        self.k1.setStyleSheet("color:white")
        self.editLine1 = QLineEdit(self)
        self.editLine1.setGeometry(100, 20, 150, 20)
        #香蕉单价
        self.k2 = QLabel(self)
        self.k2.setGeometry(30, 60, 100, 20)
        self.k2.setText('香蕉/元：')
        self.k2.setStyleSheet("color:white")
        self.editLine2 = QLineEdit(self)
        self.editLine2.setGeometry(100, 60, 150, 20)
        # 香蕉单价
        self.k3 = QLabel(self)
        self.k3.setGeometry(30, 100, 100, 20)
        self.k3.setText('西瓜/元：')
        self.k3.setStyleSheet("color:white")
        self.editLine3 = QLineEdit(self)
        self.editLine3.setGeometry(100, 100, 150, 20)
        # 香蕉单价
        self.k4 = QLabel(self)
        self.k4.setGeometry(30, 140, 100, 20)
        self.k4.setText('重量/千克：')
        self.k4.setStyleSheet("color:white")
        self.editLine4 = QLineEdit(self)
        self.editLine4.setGeometry(100, 140, 150, 20)
        #识别结果
        self.k5 = QLabel(self)
        self.k5.setGeometry(30, 180, 100, 20)
        self.k5.setText('识别结果：')
        self.k5.setStyleSheet("color:white")
        self.editLine5 = QLineEdit(self)
        self.editLine5.setGeometry(100, 180, 150, 20)
        #记重结果
        self.k6 = QLabel(self)
        self.k6.setGeometry(30, 220, 100, 20)
        self.k6.setText('记重结果：')
        self.k6.setStyleSheet("color:white")
        self.editLine6 = QLineEdit(self)
        self.editLine6.setGeometry(100, 220, 150, 20)
        # 创建标签
        self.image_label = QLabel(self)
        self.image_label.setGeometry(280, 20, 200, 200)
        # 定义按钮
        button1 = QPushButton('识别记重', self)
        button1.setGeometry(35, 260, 200, 40)
        button1.clicked.connect(self.button1_click)
        self.lb3 = QLabel(self)
        self.lb3.setGeometry(270, 10, 300, 310)
        self.lb3.setStyleSheet("border: 2px solid white")
        self.lb3.setScaledContents(True)  # 自适应QLabel大小
        # 设置窗口的位置和大小
        self.setGeometry(200, 100, 1000, 700)
        # 设置窗口的标题
        self.setWindowTitle('水果识别计重系统')
        # 显示窗口
        self.setFixedSize(600,350)
        MainWindow.setCentralWidget(self.centralwidget)
        self.show()

    def apple_text(self):
        text = self.editLine1.text()
        print(text)
        global apple
        apple = float(text)
        return apple

    def banana_text(self):
        text = self.editLine2.text()
        print(text)
        global banana
        banana = float(text)
        return banana

    def xigua_text(self):
        text = self.editLine3.text()
        print(text)
        global xigua
        xigua = float(text)
        return xigua

    def kg_text(self):
        text = self.editLine4.text()
        print(text)
        global kg
        kg = float(text)
        return kg

    def sum_shuiguo(self):
        weight = self.kg_text()
        if result == "苹果":
            apple1 = self.apple_text()

            apple_price = apple1 * weight
            return apple_price
        elif result == "香蕉":
            banana1 = self.banana_text()
            print(banana1)
            banana_price = banana1 * weight
            return banana_price
        elif result == "西瓜":
            xigua1 = self.xigua_text()
            print(xigua1)
            xigua_price = xigua1 * weight
            return xigua_price
    def button1_click(self):
        # 打开文件对话框以选择一个图片文件
        self.editLine1.textChanged.connect(self.apple_text)
        self.editLine4.textChanged.connect(self.banana_text)
        self.editLine3.textChanged.connect(self.xigua_text)
        self.editLine2.textChanged.connect(self.kg_text)
        file_dialog = QFileDialog(self)
        # 图片格式为bmp、png和jpg
        file_dialog.setNameFilter("Image files (*.bmp *.png *.jpg)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            # 加载选择的图片文件
            image_file_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(image_file_path)
            self.image_label.setGeometry(280, 20, 280, 280)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
            ImageName = "1.png"
            r = requests.post(URL, headers=getHeader(ImageName), data=getBody(filePath=image_file_path))
            # 解析JSON数据
            data = json.loads(r.content)
            data = data['data']['fileList'][0]['label']
            print(data)
            apple_arr = np.array(
                [161, 1152, 1210, 1267, 2160, 2324, 4115, 4629, 4901, 6134, 6385, 11638, 11824, 12087, 13121, 14374,
                 15504,
                 15938, 16194, 18125, 18765, 18868, 18961, 19083, 19085, 19349, 1729])
            banana_arr = np.array([185, 5862, 6511, 10202, 12999, 16983, 16988])
            watermelon_arr = np.array([832])
            # excel_file = '物体识别label返回值.xlsx'  # 替换为实际的Excel文件路径
            global result
            if data in apple_arr:
                result = "苹果"
            elif data in banana_arr:
                result = "香蕉"
            elif data in watermelon_arr:
                result = "西瓜"
            else:
                result = '识别错误'
            print(self.apple_text())

            result1 = self.sum_shuiguo()
            print(result1)


            self.editLine5.setText(result)
            self.editLine6.setText(str(result1))



        return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    system = FruitRecognitionSystem()
    system.show()
    sys.exit(app.exec_())