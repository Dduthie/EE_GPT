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
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTextEdit, QToolBar, QWidget)
import Mainwindow_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(747, 714)
        MainWindow.setDocumentMode(False)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        icon = QIcon()
        icon.addFile(u":/Settings/settings_FILL_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon)
        self.actionSettings.setMenuRole(QAction.NoRole)
        self.actionchat = QAction(MainWindow)
        self.actionchat.setObjectName(u"actionchat")
        icon1 = QIcon()
        icon1.addFile(u":/Settings/chat_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionchat.setIcon(icon1)
        self.actionchat.setMenuRole(QAction.NoRole)
        self.actionadd_chat = QAction(MainWindow)
        self.actionadd_chat.setObjectName(u"actionadd_chat")
        icon2 = QIcon()
        icon2.addFile(u":/Settings/add_comment_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionadd_chat.setIcon(icon2)
        self.actionadd_chat.setMenuRole(QAction.NoRole)
        self.actionOpen_chat = QAction(MainWindow)
        self.actionOpen_chat.setObjectName(u"actionOpen_chat")
        icon3 = QIcon()
        icon3.addFile(u":/Settings/folder_open_FILL14.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_chat.setIcon(icon3)
        self.actionOpen_chat.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.tokenLabel = QLabel(self.page)
        self.tokenLabel.setObjectName(u"tokenLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tokenLabel.sizePolicy().hasHeightForWidth())
        self.tokenLabel.setSizePolicy(sizePolicy)
        self.tokenLabel.setMinimumSize(QSize(0, 0))
        self.tokenLabel.setMaximumSize(QSize(75, 16777215))
        self.tokenLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.tokenLabel.setWordWrap(False)

        self.gridLayout_2.addWidget(self.tokenLabel, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 2, 2, 1, 1)

        self.Ouput = QTextEdit(self.page)
        self.Ouput.setObjectName(u"Ouput")
        self.Ouput.setFocusPolicy(Qt.ClickFocus)
        self.Ouput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Ouput.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Ouput.setReadOnly(True)

        self.gridLayout_2.addWidget(self.Ouput, 0, 1, 1, 2)

        self.Input = QTextEdit(self.page)
        self.Input.setObjectName(u"Input")
        sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
        self.Input.setSizePolicy(sizePolicy)
        self.Input.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Input.setAutoFormatting(QTextEdit.AutoNone)
        self.Input.setReadOnly(False)

        self.gridLayout_2.addWidget(self.Input, 1, 1, 1, 2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 747, 22))
        self.menuChat = QMenu(self.menubar)
        self.menuChat.setObjectName(u"menuChat")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuContext_Manager = QMenu(self.menubar)
        self.menuContext_Manager.setObjectName(u"menuContext_Manager")
        self.menuPrompt_Editor = QMenu(self.menubar)
        self.menuPrompt_Editor.setObjectName(u"menuPrompt_Editor")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setAllowedAreas(Qt.AllToolBarAreas)
        self.toolBar.setOrientation(Qt.Horizontal)
        self.toolBar.setIconSize(QSize(24, 24))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menuChat.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuContext_Manager.menuAction())
        self.menubar.addAction(self.menuPrompt_Editor.menuAction())
        self.menuChat.addSeparator()
        self.toolBar.addAction(self.actionOpen_chat)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.actionSettings.setToolTip(QCoreApplication.translate("MainWindow", u"change app settings", None))
#endif // QT_CONFIG(tooltip)
        self.actionchat.setText(QCoreApplication.translate("MainWindow", u"chat", None))
#if QT_CONFIG(tooltip)
        self.actionchat.setToolTip(QCoreApplication.translate("MainWindow", u"current chat", None))
#endif // QT_CONFIG(tooltip)
        self.actionadd_chat.setText(QCoreApplication.translate("MainWindow", u"add chat", None))
#if QT_CONFIG(tooltip)
        self.actionadd_chat.setToolTip(QCoreApplication.translate("MainWindow", u"add a new chat", None))
#endif // QT_CONFIG(tooltip)
        self.actionOpen_chat.setText(QCoreApplication.translate("MainWindow", u"Open chat", None))
#if QT_CONFIG(tooltip)
        self.actionOpen_chat.setToolTip(QCoreApplication.translate("MainWindow", u"Open a previous chat", None))
#endif // QT_CONFIG(tooltip)
        self.tokenLabel.setText(QCoreApplication.translate("MainWindow", u"Tokens:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text here", None))
        self.menuChat.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuContext_Manager.setTitle(QCoreApplication.translate("MainWindow", u"Context Manager", None))
        self.menuPrompt_Editor.setTitle(QCoreApplication.translate("MainWindow", u"Prompt Editor", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

