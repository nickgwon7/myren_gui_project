# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_1.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_1_MainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(910, 801)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_name = QLabel(self.centralwidget)
        self.lb_name.setObjectName(u"lb_name")
        self.lb_name.setGeometry(QRect(20, 30, 261, 16))
        self.lb_photo = QLabel(self.centralwidget)
        self.lb_photo.setObjectName(u"lb_photo")
        self.lb_photo.setGeometry(QRect(430, 90, 461, 701))
        self.lb_mobility = QLabel(self.centralwidget)
        self.lb_mobility.setObjectName(u"lb_mobility")
        self.lb_mobility.setGeometry(QRect(20, 70, 261, 16))
        self.lb_relation = QLabel(self.centralwidget)
        self.lb_relation.setObjectName(u"lb_relation")
        self.lb_relation.setGeometry(QRect(20, 110, 291, 16))
        self.lb_contact = QLabel(self.centralwidget)
        self.lb_contact.setObjectName(u"lb_contact")
        self.lb_contact.setGeometry(QRect(20, 150, 291, 16))
        self.lb_where = QLabel(self.centralwidget)
        self.lb_where.setObjectName(u"lb_where")
        self.lb_where.setGeometry(QRect(20, 200, 411, 16))
        self.btn_map = QPushButton(self.centralwidget)
        self.btn_map.setObjectName(u"btn_map")
        self.btn_map.setGeometry(QRect(70, 390, 241, 221))
        self.lb_time = QLabel(self.centralwidget)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setGeometry(QRect(660, 20, 251, 31))
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\uc0ac\uc6a9\uc790 \uc815\ubcf4", None))
        self.lb_name.setText(QCoreApplication.translate("mainWindow", u"\uc774\ub984 : ", None))
        self.lb_photo.setText(QCoreApplication.translate("mainWindow", u"TextLabel", None))
        self.lb_mobility.setText(QCoreApplication.translate("mainWindow", u"\ubaa8\ube4c\ub9ac\ud2f0 \uc815\ubcf4 : ", None))
        self.lb_relation.setText(QCoreApplication.translate("mainWindow", u"\uad00\uacc4 : ", None))
        self.lb_contact.setText(QCoreApplication.translate("mainWindow", u"\uc5f0\ub77d\ucc98 : ", None))
        self.lb_where.setText(QCoreApplication.translate("mainWindow", u"\uc0ac\uace0 \uc7a5\uc18c : ", None))
        self.btn_map.setText(QCoreApplication.translate("mainWindow", u"\uc0ac\uace0\uc7a5\uc18c \uc790\uc138\ud788\ubcf4\uae30", None))
        self.lb_time.setText(QCoreApplication.translate("mainWindow", u"\ud604\uc7ac \uc2dc\uac01 :", None))
    # retranslateUi

