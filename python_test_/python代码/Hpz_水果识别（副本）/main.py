from Hpz_UI import hpz_ui
import API
import os
import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt
import numpy as np



apple = 0
banana = 0
watermelon = 0
kg = 0
mark=0

class hpz_window(QWidget, hpz_ui):
    def __init__(self, parent=None):
        super(hpz_window, self).__init__(parent)
        self.setupUi(self)
        # 绑定按钮
        # text_xx输入文本槽函数
        self.apple.textChanged.connect(self.text_apple)
        self.banana.textChanged.connect(self.text_banana)
        self.watermelon.textChanged.connect(self.text_watermelon)
        self.kg.textChanged.connect(self.text_kg)
        # push_button槽函数
        self.recognition.clicked.connect(self.sum_return)
        self.choose.clicked.connect(self.open_photo)
        self.open.clicked.connect(self.open_camera)
        self.close.clicked.connect(self.close_camera)
        # 初始变量
        self.image_path = None
        # 标记是否已经截取了图片
        self.image_captured = False
        # 摄像头绑定
        self.cap = cv2.VideoCapture(0)
        # 创建 QTimer 对象，并将 show_from 方法绑定到 QTimer 的 timeout 信号上
        self.timer = QTimer(self)

    def close_event(self, event):
        # 删除已经保存的图片
        if os.path.exists('photo.jpg'):
            os.remove('photo.jpg')
        event.accept()

    def show_from(self):
        # if not self.cap.isOpened() or self.image_captured:
        #     return

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
            # 将 QImage 缩放为指定大小，并设置给 QLabel 控件显示出来, 将 QImage 对象缩放为指定大小，并保持宽高比。这一步是为了将图像适应 640x480 大小的显示窗口。
            p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
            # 将缩放后的图像设置为 QLabel 控件的图像显示。
            self.label.setPixmap(QPixmap.fromImage(p))

    def text_apple(self):
        text = self.apple.text()
        global apple
        try:
            apple = float(text)
        except ValueError:
            pass
        # print(apple)
        return apple

    def text_banana(self):
        text = self.banana.text()
        global banana
        try:
            banana = float(text)
        except ValueError:
            pass
        return banana

    def text_watermelon(self):
        text = self.watermelon.text()
        global watermelon
        try:
            watermelon = float(text)
        except ValueError:
            pass
        return watermelon

    def text_kg(self):
        text = self.kg.text()
        global kg
        try:
            kg = float(text)
        except ValueError:
            pass
        return kg

    def open_photo(self):
        if os.path.exists('photo.jpg'):
            os.remove('photo.jpg')
        if self.cap.isOpened():
            self.timer.stop()
        file_dialog = QFileDialog()
        # 设置默认路径和过滤器，这行代码的作用是打开一个文件对话框，让用户选择图片文件，并返回用户所选择的图片文件名。
        image_path, _ = file_dialog.getOpenFileName(self, "Open Image", "~/Pictures",
                                                    "Image Files (*.png *.jpg *.jpeg)")

        # 如果有选择文件
        if image_path:
            # 创建 QPixmap 对象，用于加载图片,加载后的图片可以用于设置标签、按钮或其他可显示图片的 Qt 控件的图像内容。
            pixmap = QPixmap(image_path)
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)
        self.image_path = image_path
        return image_path

    def get_picture(self):
        global mark
        mark+=1
        if mark%250==0 :
            ret, frame = self.cap.read()
            if ret:
                # 这行代码的作用是将从摄像头读取到的图像数据（frame）保存为名为 'photo.jpg' 的文件
                cv2.imwrite('photo.jpg', frame)
                self.result_text()
                self.sum_return()




    def open_camera(self):

            self.timer.timeout.connect(self.show_from)
            self.timer.timeout.connect(self.get_picture)
            self.timer.start(10)



    def close_camera(self,event):
        if os.path.exists('photo.jpg'):
            os.remove('photo.jpg')
        if self.cap.isOpened():
            self.timer.stop()


    def sum_return(self):
        # print(self.sum_result())
        path_result = self.result_path()
        self.recognize.setText(path_result)
        result_true = self.sum_result()
        self.result.setText(str(result_true))
        apple2 = self.text_apple()
        banana2=self.text_banana()
        print(apple2+banana2)

    def result_text(self):
        path_result = self.result_path()
        self.recognize.setText(path_result)

    def sum_result(self):
        true_path = self.result_path()
        kg1 = self.text_kg()
        if apple == 0 or banana == 0 or watermelon == 0 or kg == 0:
            return "请输入价格"
        elif true_path == '苹果':
            apple1 = self.text_apple()
            apple_sum = apple1 * kg1
            return apple_sum
        elif true_path == '香蕉':
            banana1 = self.text_banana()
            banana_sum = banana1 * kg1
            return banana_sum
        elif true_path == '西瓜':
            watermelon1 = self.text_watermelon()
            watermelon_sum = watermelon1 * kg1
            return watermelon_sum
        else:
            return "无法计重"

    def result_path(self):
        if os.path.exists('photo.jpg'):
            img = 'photo.jpg'
        else:
            img = self.image_path
        print(img)
        label_true = API.api_get().label_get(img)
        # 打印识别出的label值
        print(label_true)

        apple_arr = np.array(
            [161, 1152, 1210, 1267, 2160, 2324, 4115, 4629, 4901, 6134, 6385, 11638, 11824, 12087, 13121, 14374, 15504,
             15938, 16194, 18125, 18765, 18868, 18961, 19083, 19085, 19349, 1729,4778])
        banana_arr = np.array([185, 5862, 6511, 10202, 12999, 16983, 16988,9177])
        watermelon_arr = np.array([832,19434,8685,135,16531,18702,19435,20017,4601])

        if label_true in apple_arr:
            result = "苹果"
        elif label_true in banana_arr:
            result = "香蕉"
        elif label_true in watermelon_arr:
            result = "西瓜"
        else:
            result = '识别错误'
        return result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = hpz_window()
    window.show()
    sys.exit(app.exec_())
