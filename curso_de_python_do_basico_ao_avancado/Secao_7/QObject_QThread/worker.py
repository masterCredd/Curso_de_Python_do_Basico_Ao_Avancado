# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_myWidget(object):
    def setupUi(self, myWidget):
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(400, 312)
        font = QFont()
        font.setPointSize(40)
        myWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(myWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_1 = QLabel(myWidget)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout_2.addWidget(self.label_1, 0, 1, 1, 1)

        self.label_2 = QLabel(myWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.button_1 = QPushButton(myWidget)
        self.button_1.setObjectName(u"button_1")

        self.gridLayout_2.addWidget(self.button_1, 1, 1, 1, 1)

        self.button_2 = QPushButton(myWidget)
        self.button_2.setObjectName(u"button_2")

        self.gridLayout_2.addWidget(self.button_2, 1, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(myWidget)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi

    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(QCoreApplication.translate("myWidget", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("myWidget", u"L_1", None))
        self.label_2.setText(QCoreApplication.translate("myWidget", u"L_2", None))
        self.button_1.setText(QCoreApplication.translate("myWidget", u"B_1", None))
        self.button_2.setText(QCoreApplication.translate("myWidget", u"B_2", None))
    # retranslateUi

