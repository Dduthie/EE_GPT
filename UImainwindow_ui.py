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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QGridLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QStatusBar, QTextEdit, QToolBar,
    QWidget)
import Mainwindow_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(772, 730)
        icon = QIcon()
        icon.addFile(u":/Icons/Resources/artificial-intelligence-48.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Resources/settings_FILL_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionSettings.setMenuRole(QAction.NoRole)
        self.actionchat = QAction(MainWindow)
        self.actionchat.setObjectName(u"actionchat")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Resources/chat_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionchat.setIcon(icon2)
        self.actionchat.setMenuRole(QAction.NoRole)
        self.actionadd_chat = QAction(MainWindow)
        self.actionadd_chat.setObjectName(u"actionadd_chat")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Resources/chat_add_on_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionadd_chat.setIcon(icon3)
        self.actionadd_chat.setMenuRole(QAction.NoRole)
        self.actionOpen_chat = QAction(MainWindow)
        self.actionOpen_chat.setObjectName(u"actionOpen_chat")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Resources/folder_open_FILL14.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_chat.setIcon(icon4)
        self.actionOpen_chat.setMenuRole(QAction.NoRole)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Resources/save_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon5)
        self.actionSave.setMenuRole(QAction.NoRole)
        self.actionFont = QAction(MainWindow)
        self.actionFont.setObjectName(u"actionFont")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Resources/font_download_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFont.setIcon(icon6)
        self.actionFont.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(17)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Ouput = QTextEdit(self.page)
        self.Ouput.setObjectName(u"Ouput")
        self.Ouput.setFocusPolicy(Qt.ClickFocus)
        self.Ouput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Ouput.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Ouput.setReadOnly(True)

        self.gridLayout_2.addWidget(self.Ouput, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)

        self.Input = QTextEdit(self.page)
        self.Input.setObjectName(u"Input")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
        self.Input.setSizePolicy(sizePolicy)
        self.Input.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Input.setAutoFormatting(QTextEdit.AutoNone)
        self.Input.setReadOnly(False)

        self.gridLayout_2.addWidget(self.Input, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox = QComboBox(self.page_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.comboBox.setFont(font1)

        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.horizontalSlider = QSlider(self.page_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background: red;\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 4px; right: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: pink;\n"
"}\n"
"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider, 3, 0, 1, 1)

        self.verticalSlider = QSlider(self.page_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: red;\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 4px; right: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: pink;\n"
"}")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_3.addWidget(self.verticalSlider, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 22))
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolBar_2.sizePolicy().hasHeightForWidth())
        self.toolBar_2.setSizePolicy(sizePolicy2)
        self.toolBar_2.setMinimumSize(QSize(0, 0))
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menuChat.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuContext_Manager.menuAction())
        self.menubar.addAction(self.menuPrompt_Editor.menuAction())
        self.menuChat.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionOpen_chat)
        self.toolBar_2.addAction(self.actionchat)
        self.toolBar_2.addAction(self.actionadd_chat)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionSettings)
        self.toolBar_2.addAction(self.actionFont)

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
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"save current chat", None))
#endif // QT_CONFIG(tooltip)
        self.actionFont.setText(QCoreApplication.translate("MainWindow", u"Font", None))
#if QT_CONFIG(tooltip)
        self.actionFont.setToolTip(QCoreApplication.translate("MainWindow", u"Change font", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text here", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ChatGPT 3.5", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ChatGPT 3.5 16k", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"ChatGPT 4", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"ChatGPT 4 32k", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.menuChat.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuContext_Manager.setTitle(QCoreApplication.translate("MainWindow", u"Context Manager", None))
        self.menuPrompt_Editor.setTitle(QCoreApplication.translate("MainWindow", u"Prompt Editor", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

