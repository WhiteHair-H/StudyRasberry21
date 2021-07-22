import io
import sys
import folium
from PyQt5 import QtWidgets , QtWebEngineWidgets

app = QtWidgets.QApplication(sys.argv) # QT 윈폼 생성

m = folium.Map(location=[35.566345, 126.977893], zoom_start=12 , tiles='Cartodb Positron') ## folium 맵 생성

data = io.BytesIO() # byte로
m.save(data, close_file=False) # 맵 데이터 저장

win = QtWebEngineWidgets.QWebEngineView() # QT5 웹엔진 생성
win.setHtml(data.getvalue().decode()) ## 바이너리 맵데이터를 HTML 재변환
win.resize(800, 600) # 윈폼크기 조정
win.show()

sys.exit(app.exec_())
