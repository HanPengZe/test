import os
import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt
import numpy as np
import API  # 导入外接API
from QT import Ui_Form  # 导入UI界面

# 初始化变量
text_apple = 0
text_banana = 0
text_watermelon = 0
text_kg = 0


class MyWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        # 绑定按钮
        self.chooseButton.clicked.connect(self.open_image)
        self.open.clicked.connect(self.open_camera)
        self.shot.clicked.connect(self.capture_image)
        self.recognition.clicked.connect(self.true_result)
        self.recognition.clicked.connect(self.path_result)
        self.apple.textChanged.connect(self.text_changed_apple)
        self.banana.textChanged.connect(self.text_changed_banana)
        self.watermelon.textChanged.connect(self.text_changed_watermelon)
        self.kg.textChanged.connect(self.text_changed_kg)
        # 初始变量
        self.image_path = None
        # 标记是否已经截取了图片
        self.image_captured = False
        # 摄像头绑定
        self.cap = cv2.VideoCapture(0)
        # 创建 QTimer 对象，并将 display_frame 方法绑定到 QTimer 的 timeout 信号上
        self.timer = QTimer(self)

    def closeEvent(self, event):
        # 删除已经保存的图片
        if os.path.exists('photo.jpg'):
            os.remove('photo.jpg')

        event.accept()

    def display_frame(self):
        if not self.cap.isOpened() or self.image_captured:
            return

        ret, frame = self.cap.read()
        if ret:
            # 将 BGR 格式的帧转换为 RGB 格式
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 获取帧的高度、宽度和通道数
            h, w, ch = frame.shape
            # 计算每行像素所占的字节数
            bytesPerLine = ch * w
            # 创建 QImage 对象，并将帧数据填充到 QImage 中
            convertToQtFormat = QImage(frame.data, w, h, bytesPerLine, QImage.Format_RGB888)
            # 将 QImage 缩放为指定大小，并设置给 QLabel 控件显示出来
            p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
            self.label.setPixmap(QPixmap.fromImage(p))

    # 打开摄像头
    def open_camera(self):
        self.timer.timeout.connect(self.display_frame)
        # 每隔 30 毫秒触发一次 QTimer 的 timeout 信号，显示摄像头捕获的帧
        self.timer.start(30)

    def capture_image(self):
        # 捕获摄像头的当前帧，并保存到文件中
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite('photo.jpg', frame)
            # 释放摄像头对象，停止显示摄像头捕获的帧
            self.cap.release()
            self.image_captured = True

    # 返回函数sum结果到对应文本框
    def true_result(self):
        result_true = self.sum_result()
        self.result.setText(str(result_true))

    # 苹果输入文本框
    def text_changed_apple(self):
        text = self.apple.text()
        global text_apple
        try:
            text_apple = float(text)
        except ValueError:
            pass
        return text_apple

    # 香蕉输入框
    def text_changed_banana(self):
        text = self.banana.text()
        global text_banana
        try:
            text_banana = float(text)
        except ValueError:
            pass
        return text_banana

    # 西瓜输入框
    def text_changed_watermelon(self):
        text = self.watermelon.text()
        global text_watermelon
        try:
            text_watermelon = float(text)
        except ValueError:
            pass
        return text_watermelon

    # 重量输入框
    def text_changed_kg(self):
        text = self.kg.text()
        global text_kg
        try:
            text_kg = float(text)
        except ValueError:
            pass
        return text_kg

    # 打开相片
    def open_image(self):
        if os.path.exists('photo.jpg'):
            os.remove('photo.jpg')
        # 创建 QFileDialog 对象
        file_dialog = QFileDialog()

        # 设置默认路径和过滤器
        image_path, _ = file_dialog.getOpenFileName(self, "Open Image", "~/Pictures",
                                                    "Image Files (*.png *.jpg *.jpeg)")

        # 如果有选择文件
        if image_path:
            # 创建 QPixmap 对象，用于加载图片
            pixmap = QPixmap(image_path)

            # 将图片自适应缩放，并设置给 image_label 控件
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)
        self.image_path = image_path
        return image_path

    # 识别结果
    def result_path(self):

        if os.path.exists('photo.jpg'):
            img = 'photo.jpg'
        else:
            img = self.image_path

        label_true = API.CurrencyLabelDetector().get_currency_label(img)
        # 打印识别出的label值
        print(label_true)

        apple_arr = np.array(
            [161, 1152, 1210, 1267, 2160, 2324, 4115, 4629, 4901, 6134, 6385, 11638, 11824, 12087, 13121, 14374, 15504,
             15938, 16194, 18125, 18765, 18868, 18961, 19083, 19085, 19349, 1729])
        banana_arr = np.array([185, 5862, 6511, 10202, 12999, 16983, 16988])
        watermelon_arr = np.array([832])

        if label_true in apple_arr:
            result = "苹果"
        elif label_true in banana_arr:
            result = "香蕉"
        elif label_true in watermelon_arr:
            result = "西瓜"
        else:
            result = '识别错误'
        return result

    # 返回函数num结果到对应文本框
    def path_result(self):
        path_result = self.result_path()
        self.recognize.setText(path_result)

    # 计重结果
    def sum_result(self):
        true_path = self.result_path()
        kg = self.text_changed_kg()
        if text_apple == 0 or text_banana == 0 or text_watermelon == 0 or text_kg == 0:
            return "请输入价格"
        elif true_path == '苹果':
            apple = self.text_changed_apple()
            apple_sum = apple * kg
            return apple_sum
        elif true_path == '香蕉':
            banana = self.text_changed_banana()
            banana_sum = banana * kg
            return banana_sum
        elif true_path == '西瓜':
            watermelon = self.text_changed_watermelon()
            watermelon_sum = watermelon * kg
            return watermelon_sum
        else:
            return "无法计重"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
