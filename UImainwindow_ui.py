# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UImainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 644)
        self.actionPDF_Chat = QAction(MainWindow)
        self.actionPDF_Chat.setObjectName(u"actionPDF_Chat")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.Ouput = QTextEdit(self.centralwidget)
        self.Ouput.setObjectName(u"Ouput")
        self.Ouput.setFocusPolicy(Qt.ClickFocus)
        self.Ouput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Ouput.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Ouput.setReadOnly(True)

        self.gridLayout.addWidget(self.Ouput, 1, 1, 1, 2)

        self.Input = QTextEdit(self.centralwidget)
        self.Input.setObjectName(u"Input")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
        self.Input.setSizePolicy(sizePolicy)
        self.Input.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Input.setAutoFormatting(QTextEdit.AutoNone)
        self.Input.setReadOnly(False)

        self.gridLayout.addWidget(self.Input, 2, 1, 1, 2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 22))
        self.menuChat = QMenu(self.menubar)
        self.menuChat.setObjectName(u"menuChat")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuChat.menuAction())
        self.menuChat.addAction(self.actionPDF_Chat)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionPDF_Chat.setText(QCoreApplication.translate("MainWindow", u"PDF Chat", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Darian's Brain 2.0", None))
        self.Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tokens", None))
        self.menuChat.setTitle(QCoreApplication.translate("MainWindow", u"Chat", None))
    # retranslateUi

