import sys, os

from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PySide6 import QtWidgets
from ui import Ui_MainWindow
from ui_1 import Ui_1_MainWindow

from PySide6.QtCore import QTimer # 타이머 기능 활성화 위해 선언
from tkinter import Widget  #현재 시각 가져오기 위해 선언
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from urllib.request import Request, urlopen
from PySide6.QtGui import *

import time


def find(chrome, css):
    wait = WebDriverWait(chrome, 5)
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def find_all(chrome, css):
    find(chrome, css) # 일단 기다리기
    return chrome.find_elements_by_css_selector(css)

user_Info = [

    {"name" : "최웅", "mobility_Info" : "차", "relation" : "친구", "contact" : "010-1234-1234", "where" : "경기도 시흥시 대야동 332-116", "image_path" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvLdUtSTkMBCm72Q-4sjW7Tq564xt5ktxKfg&usqp=CAU"},
    {"name" : "국연수", "mobility_Info" : "휠체어", "relation" : "모", "contact" : "010-1111-1234", "where" : "원초로 9", "image_path" : "https://w.namu.la/s/8e499b5b80829463844f191e5db50c7b17223e45853dc2011b0670ec967229b54d6a7c3a5d82aa2292847f1b3ab9a07dfaeea94edcb716a4a4493a90aa407570b8e1348b6e86aec44146f48d6bc76fe1d5bf69a1bfb24890190750fdd54f688b"},
    {"name" : "솔이", "mobility_Info" : "보행자", "relation" : "부", "contact" : "010-2222-5678", "where" : "서울특별시 도봉구 덕릉로 257", "image_path" : "https://w.namu.la/s/6e9dfbe506f769822a8d8c95ec229b41b243222f031db4590c9e032a2fc3f0421b63a039b5e092dce3c8088347988a20459ed498e704a724413cd732afb24284c3746139fef9218a73c9194c3b1c69832a0c3ca743686e3ab333745228588e45"}
]


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 현재 시각 표시 
        self.timer = QTimer()
        self.timer.setInterval(900) # 대략 10ms의 delay를 고려하여 1초를 만들기 위해 선언
        self.timer.timeout.connect(self.tick)
        self.timer.start()   
    
        # table show (데이터를 몇 초 간격으로 업로드하고 싶으면 QTimer 이용)
        self.ui.table.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.table.setRowCount(len(user_Info))
        for r, u in enumerate(user_Info): # 인덱스 값까지 함께 가져오기 위해서 enumerate 사용
            self.ui.table.setItem(r, 0, QTableWidgetItem(u["name"])) # QTableWidgetItem의 값은 무조건 string type이여야 한다.
            self.ui.table.setItem(r, 1, QTableWidgetItem(u["mobility_Info"]))
            self.ui.table.setItem(r, 2, QTableWidgetItem(u["relation"]))
            self.ui.table.setItem(r, 3, QTableWidgetItem(str(u["contact"])))
            self.ui.table.setItem(r, 4, QTableWidgetItem(u["where"]))

        self.ui.table.cellDoubleClicked.connect(self.location_Info)    
         
        
    
    def tick(self):
        now = datetime.datetime.now()
        self.ui.lb_now.setText(f"현재 시각 : {now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}")
    
    
    def location_Info(self, r, c):
        
        window_1.show()

        # 테이블에서 클릭된 행에 대한 데이터를 보낼 때 사용해야 됨
        # Info = user_Info[r]
        # where = Info["where"]
        



class MainWindow_1(QMainWindow):
    def __init__(self):
        super(MainWindow_1, self).__init__()
        self.ui_1 = Ui_1_MainWindow()
        self.ui_1.setupUi(self)

        self.timer = QTimer()
        self.timer.setInterval(900) # 대략 10ms의 delay를 고려하여 1초를 만들기 위해 선언
        self.timer.timeout.connect(self.tick)
        self.timer.start() 


        # self.ui_1.lb_name.setText(f"이름 : {user_Info[0]["name"]}")
        self.ui_1.lb_name.setText(f"이름 : 국연수")
        self.ui_1.lb_mobility.setText(f"모빌리티 정보 : 휠체어")
        self.ui_1.lb_relation.setText(f"관계 : 모")
        self.ui_1.lb_contact.setText(f"연락처 : 010-1111-1234")
        self.ui_1.lb_where.setText(f"사고 장소 : 원초로 9")

        self.ui_1.btn_map.clicked.connect(self.open_map)
        

        # #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
        # self.ui_1.qPixmapFileVar = QPixmap()
        # self.ui_1.qPixmapFileVar.load("국연수.jpg")
        # self.ui_1.qPixmapFileVar = self.ui_1.qPixmapFileVar.scaledToWidth(600)
        # self.ui_1.lb_photo.setPixmap(self.ui_1.qPixmapFileVar)

        #Web에서 Image 정보 로드

        urlString = "https://w.namu.la/s/8e499b5b80829463844f191e5db50c7b17223e45853dc2011b0670ec967229b54d6a7c3a5d82aa2292847f1b3ab9a07dfaeea94edcb716a4a4493a90aa407570b8e1348b6e86aec44146f48d6bc76fe1d5bf69a1bfb24890190750fdd54f688b"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
        request = Request(urlString, headers=headers)
        imageFromWeb = urlopen(request).read()

        #웹에서 Load한 Image를 이용하여 QPixmap에 사진데이터를 Load하고, Label을 이용하여 화면에 표시
        self.ui_1.qPixmapWebVar = QPixmap()
        self.ui_1.qPixmapWebVar.loadFromData(imageFromWeb)
        self.ui_1.qPixmapWebVar = self.ui_1.qPixmapWebVar.scaledToWidth(600)
        self.ui_1.lb_photo.setPixmap(self.ui_1.qPixmapWebVar)

    def tick(self):
        now = datetime.datetime.now()
        self.ui_1.lb_time.setText(f"현재 시각 : {now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}")

    def open_map(self):

        # exe 파일로 만들기 위해 C드라이브에 크롬드라이버를 위치시켜야한다.
        if getattr(sys, 'frozen', False):
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            chrome = webdriver.Chrome(chromedriver_path)
        else:
            chrome = webdriver.Chrome()


        link = "file:///C:/Users/nickgwon/Desktop/kakao_map/index.html"
        chrome.get(link)


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    window_1 = MainWindow_1()
    

    sys.exit(app.exec())
