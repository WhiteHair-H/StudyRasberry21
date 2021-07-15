## QT5 사용자 윈도우 구성 예제
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #self = C# - this
        self.setWindowTitle("My QT5 window") # 제목 표시줄
        self.setGeometry(80 , 80 , 600 , 300) #x , y , width , height
        self.setWindowIcon(QIcon('./image/chart.png'))

        # label add
        self.label = QLabel('메시지: ', self)
        self.label.move(10 , 10)
        self.label.setFixedSize(QSize(300, 20))
        #self.label.setGeometry(10, 10, 300 , 20)

        #button add
        self.btn = QPushButton('Click', self)
        self.btn.move(10, 50)

        # signal add = 이벤트
        self.btn.clicked.connect(self.btn_clicked)

    # Button 클릭 시그널(이벤트)
    def btn_clicked(self):
        self.label.clear()
        self.label.setText('메시지: 버튼 클릭!!')

app = QApplication(sys.argv)

win = MyWindow()
win.show()
app.exec_()