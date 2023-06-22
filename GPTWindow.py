from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread, Signal,QResource)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform,QTextCursor,QSyntaxHighlighter, QTextCharFormat, QColor,QKeyEvent)
from PySide6 import QtGui
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QTextEdit,
    QWidget,QFontDialog)
from PySide6 import QtCore

#  pyuic6 -o UImainwindow.py -x UImainwindow.ui   
import sys
from UImainwindow_ui import Ui_MainWindow
from EEGPT import EEGPT
import qdarktheme
import sys
import os
from helperClasses import SVG
from Config import Configurator

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Worker(QThread):
    result_ready = Signal(object)
    tokens_ready = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.input_text = ''

    def set_input_text(self, text):
        self.input_text = text

    def run(self):
        print(bot.messages)
        for res in bot.GPT(self.input_text):
            self.result_ready.emit(res)
        self.result_ready.emit('\n')

        num = bot.get_tokens()
        self.tokens_ready.emit(num)
        # self.result_ready.emit(result)

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.scrollFollow = True
        self.Input.installEventFilter(self)
        self.insertTextWorker = Worker()
        self.insertTextWorker.result_ready.connect(self.handle_worker_result)
        self.insertTextWorker.tokens_ready.connect(self.update_tokens)
        self.update_tokens(0)
        self.actionFont.triggered.connect(self._setFont)
        self.pushButton.released.connect(self.send_message)
        self.splitter.setSizes([400,50])
        # self.actionSettings.setIcon()
        self.actionchat.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.actionSettings.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.numChats = 0
        self.actionadd_chat.triggered.connect(self.addChat)
    
    def addChat(self):
        self.numChats+=1
        pageN = QWidget()
        layout = QGridLayout(pageN)
        pageN.setObjectName(f"page_{self.numChats}")
        
        for widg in self.stackedWidget.children():
            clone = widg.clone()
            layout.addWidget(clone)
        self.stackedWidget.addWidget(pageN)
        self.stackedWidget.setCurrentIndex(2)
           
        
    
    def _setFont(self):
        ok,self.newFont = QFontDialog.getFont()
        self.Input.setFont(self.newFont)
        self.Ouput.setFont(self.newFont)
        # app.setFont(self.newFont)
        
    def colourTest(self):
        self.variable = QAction(QIcon('Resources/save_FILL1_24.svg'),'variable')
        
        self.toolBar.addAction(self.variable)
        
    def eventFilter(self, obj:QTextEdit, event:QKeyEvent):
        if event.type() == QtCore.QEvent.Type.KeyPress and obj is self.Input:
            if ((event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter) and not event.modifiers() == QtCore.Qt.KeyboardModifier.ShiftModifier) and self.Input.hasFocus():
                self.send_message()
                return True
        return super().eventFilter(obj,event)

    def send_message(self):
        input_text = self.Input.toPlainText()
        # set background colour fo the text to blue 
        blueHighlight = '<span style="background-color:#0E3A8F;">{}</span><br><br>'

        self.Ouput.append(blueHighlight.format('> ' + input_text )+ '\n\n')
        self.Ouput.ensureCursorVisible()

        self.Input.clear()
        # Reset the background color of the text edit
        self.Ouput.setStyleSheet("")
        QApplication.processEvents()
        self.insertTextWorker.set_input_text(input_text)
        self.insertTextWorker.start()      

    def handle_worker_result(self, result):
        scrollbar = self.Ouput.verticalScrollBar()
        if self.scrollFollow:
            self.Ouput.ensureCursorVisible()
            self.Ouput.moveCursor(QtGui.QTextCursor.End)

        self.Ouput.insertPlainText(result)

    def update_tokens(self,num):
        self.statusBar().showMessage(f"Tokens: {num}/4096")

    def startupSettings(self):
        settingsDict = config.settingsDict
        
        self.resize(settingsDict['width'],settingsDict['height'])
        qdarktheme.setup_theme(settingsDict['theme'])
        self.SVGcls = SVG(settingsDict['icon'])
        self.changeColours(settingsDict['icon'])

    def changeColours(self,colour):
        self.SVGcls.changeColour(colour)

        icon1 = QIcon()
        icon1.addFile(u"./Resources/settings_FILL_24.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.actionSettings.setIcon(icon1)

        icon2 = QIcon()
        icon2.addFile(u"./Resources/chat_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionchat.setIcon(icon2)

        icon3 = QIcon()
        icon3.addFile(u"./Resources/chat_add_on_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionadd_chat.setIcon(icon3)

        icon4 = QIcon()
        icon4.addFile(u"./Resources/folder_open_FILL14.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_chat.setIcon(icon4)

        icon5 = QIcon()
        icon5.addFile(u"./Resources/save_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon5)

        icon6 = QIcon()
        icon6.addFile(u"./Resources/font_download_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFont.setIcon(icon6)       

    def closeEvent(self, event):
        # Perform any necessary saving or cleanup operations here
        settingsDict = {}
        settingsDict['width'] = str(self.width())
        settingsDict['height'] = str(self.height())
        settingsDict['icon'] = 'FFFFFF'
        settingsDict['theme'] ='auto'
        config.setUserSettings(settingsDict)
        event.accept()


if __name__ == "__main__":
    cwd = os.getcwd()
    bot = EEGPT()
    config = Configurator()
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.startupSettings()
    #qdarktheme.setup_theme(custom_colors={"primary": "#DC7633"})

    window.show()

    sys.exit(app.exec())
