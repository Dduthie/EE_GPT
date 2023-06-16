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
import Resources.Mainwindow_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(650, 644)
        MainWindow.setDocumentMode(False)
        self.actionPDF_Chat = QAction(MainWindow)
        self.actionPDF_Chat.setObjectName(u"actionPDF_Chat")
        self.actionReset_View = QAction(MainWindow)
        self.actionReset_View.setObjectName(u"actionReset_View")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionOutput_to_txt = QAction(MainWindow)
        self.actionOutput_to_txt.setObjectName(u"actionOutput_to_txt")
        self.actionSave_Conversation = QAction(MainWindow)
        self.actionSave_Conversation.setObjectName(u"actionSave_Conversation")
        self.actionLoad_Conversation = QAction(MainWindow)
        self.actionLoad_Conversation.setObjectName(u"actionLoad_Conversation")
        self.actionChange_Personality = QAction(MainWindow)
        self.actionChange_Personality.setObjectName(u"actionChange_Personality")
        self.actionModel_Options = QAction(MainWindow)
        self.actionModel_Options.setObjectName(u"actionModel_Options")
        self.actionPreferences_2 = QAction(MainWindow)
        self.actionPreferences_2.setObjectName(u"actionPreferences_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Ouput = QTextEdit(self.centralwidget)
        self.Ouput.setObjectName(u"Ouput")
        self.Ouput.setFocusPolicy(Qt.ClickFocus)
        self.Ouput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Ouput.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Ouput.setReadOnly(True)

        self.gridLayout.addWidget(self.Ouput, 0, 1, 1, 2)

        self.tokenLabel = QLabel(self.centralwidget)
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

        self.gridLayout.addWidget(self.tokenLabel, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.Input = QTextEdit(self.centralwidget)
        self.Input.setObjectName(u"Input")
        sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
        self.Input.setSizePolicy(sizePolicy)
        self.Input.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Input.setAutoFormatting(QTextEdit.AutoNone)
        self.Input.setReadOnly(False)

        self.gridLayout.addWidget(self.Input, 1, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 22))
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
        QWidget.setTabOrder(self.Input, self.pushButton)

        self.menubar.addAction(self.menuChat.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuContext_Manager.menuAction())
        self.menubar.addAction(self.menuPrompt_Editor.menuAction())
        self.menuChat.addAction(self.actionSave_Conversation)
        self.menuChat.addAction(self.actionLoad_Conversation)
        self.menuChat.addSeparator()
        self.menuChat.addAction(self.actionOutput_to_txt)
        self.menuEdit.addAction(self.actionChange_Personality)
        self.menuEdit.addAction(self.actionModel_Options)
        self.menuEdit.addAction(self.actionPreferences_2)
        self.menuView.addAction(self.actionReset_View)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionPDF_Chat.setText(QCoreApplication.translate("MainWindow", u"PDF Chat", None))
        self.actionReset_View.setText(QCoreApplication.translate("MainWindow", u"Reset View", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionOutput_to_txt.setText(QCoreApplication.translate("MainWindow", u"Output to .txt", None))
        self.actionSave_Conversation.setText(QCoreApplication.translate("MainWindow", u"Save Conversation", None))
        self.actionLoad_Conversation.setText(QCoreApplication.translate("MainWindow", u"Load Conversation", None))
        self.actionChange_Personality.setText(QCoreApplication.translate("MainWindow", u"Change Personality", None))
        self.actionModel_Options.setText(QCoreApplication.translate("MainWindow", u"Model Options", None))
        self.actionPreferences_2.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.tokenLabel.setText(QCoreApplication.translate("MainWindow", u"Tokens:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text here", None))
        self.menuChat.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuContext_Manager.setTitle(QCoreApplication.translate("MainWindow", u"Context Manager", None))
        self.menuPrompt_Editor.setTitle(QCoreApplication.translate("MainWindow", u"Prompt Editor", None))
    # retranslateUi

