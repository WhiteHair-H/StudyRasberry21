from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from naverSearch import *
import webbrowser

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./pyqt_app/naverSearch.ui',self)   

        #UI 에 있는 위젯하고 시그널 처리
        self.btnSearch.clicked.connect(self.btnSearch_Clicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResult_Selected)
        self.txtSearchWord.returnPressed.connect(self.btnSearch_Clicked) # enter 눌렀을때 검색


    def tblResult_Selected(self):
        selected =self.tblResult.currentRow() # 현재 선택된 열의 인덱스
        url = self.tblResult.item(selected , 1).text()
        #QMessageBox.about(self, 'url', url)
        webbrowser.open(url)

    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(result))

        self.tblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])
        
        n = 0
        for post in result:
            title = post['title'].replace('&lt;' ,'<').replace('&gt;' , '>').replace('<b>', '').replace('</b>', '').replace('&quot;', "'")
            self.tblResult.setItem(n, 0, QTableWidgetItem(post['title']))
            self.tblResult.setItem(n, 1, QTableWidgetItem(post['originallink']))
            n += 1
        self.tblResult.setColumnWidth(0, 500) # 0번째 컬럼은 200사이즈
        self.tblResult.setColumnWidth(1, 500) # 1번째 컬럼은 200사이즈
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼데이터 수정 금지 = C# Readonly
        

    def btnSearch_Clicked(self):
        api = naverSearch()
        jsonResult = []
        sNode ='news'
        search_word = self.txtSearchWord.text()
        display = 100

        if len(search_word) == 0:
            QMessageBox.about(self, 'popup', '검색어를 입력하세요')
            return

        # 네이버 api 검색
        jsonSearch = api.getNaverSearchresult(sNode,search_word, 1, display)
        jsonResult = jsonSearch['items'] # items리스트 분리
        print(len(jsonResult))
        self.statusbar.showMessage('검색결과 : {0}개'.format(len(jsonResult)))
        # model = QtGui.QStandardItemModel() # 리스트형식으로 변환
        # self.tblResult.setModel(model) #  연결

        # for post in jsonResult:
        #     item = QtGui.QStandardItem(post['title'])
        #     model.appendRow(item)

        self.makeTable(jsonResult)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())