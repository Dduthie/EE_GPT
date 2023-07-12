from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread, Signal,QResource,Slot)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform,QTextCursor,QSyntaxHighlighter, QTextCharFormat, QColor,QKeyEvent,QGuiApplication)
from PySide6 import QtGui
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QTextEdit,
    QWidget,QFontDialog,QFileDialog,QColorDialog)
from PySide6 import QtCore


import sys
from UImainwindow_ui import Ui_Mainwindow
from EEGPT import EEGPT
import qdarktheme
import sys
import os
from helperClasses import SVG
from Config import Configurator
import pickle
from conversations import convoManager

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
        convoManager.addUserChat(text)

    def run(self):
        for res in bot.GPT():
            self.result_ready.emit(res)
        self.result_ready.emit('\n')

        num = bot.get_tokens()
        self.tokens_ready.emit(num)

class Mainwindow(QMainWindow, Ui_Mainwindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.scrollFollow = True
        self.Input.installEventFilter(self)
        self.Input.setFocus()

        self.insertTextWorker = Worker()
        self.insertTextWorker.result_ready.connect(self.handle_worker_result)
        self.insertTextWorker.tokens_ready.connect(self.update_tokens)
        self.update_tokens(0)

        self.actionFont.triggered.connect(self._setFont)
        self.fontbutton.released.connect(self._setFont)
        self.paletteButton.released.connect(self._setColour)
        self.submit_Button.released.connect(self.send_message)
        self.reset_Button.released.connect(self.resetButton)

        self.splitter.setSizes([400,50])

        self.actionchat.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.actionchat.triggered.connect(self.changeChat)
        self.actionchat.setCheckable(True)
        self.actionchat.setChecked(True)
        self.actionSettings.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.actionReset_View.triggered.connect(self.resetView)
        self.actionReset_View.setShortcut(Qt.Key.Key_F10)
        self.actionFullscreen.setShortcut(Qt.Key.Key_F11)
        self.actionFullscreen.triggered.connect(self.fullScreen)
        self.actionDelete.triggered.connect(self.removeChat)
        self.actionadd_chat.triggered.connect(self.addChat)
        self.actionSave.triggered.connect(self.saveGPT)
        self.actionOpen_chat.triggered.connect(self.loadGPT)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        spacer.objectName = 'spacer'
        self.toolBar_2.insertWidget(self.toolBar_2.actions()[-4],spacer)

    @Slot()
    def test(self):
        self.changeColours('000000')

    @Slot()
    def saveGPT(self):
        filename = QFileDialog.getSaveFileName(self,
            "Save Chat", "/home/", "Chat Files (*.gpt)")
        if filename[0]:
            convoManager.saveConversation(filename[0],self.Ouput.toHtml())

    @Slot()
    def loadGPT(self):
        query = QFileDialog.getOpenFileNames(self,
            "Load Chat", "/home/", "Chat Files (*.gpt)")
        filenames = query[0]
        if filenames:
            self.toolBar_2.actions()[convoManager.getCurrentConversationID()].setChecked(False)
            action = QAction(QIcon(u"./Resources/chat_FILL1_24.svg"), "New chat", self)
            action.triggered.connect(self.changeChat)
            action.setCheckable(True)
            action.setChecked(True)
            action.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
            self.toolBar_2.insertAction(self.toolBar_2.actions()[-6], action)

            if len(filenames)==1:
                convoManager.loadConversation(filenames[0],self.Ouput.toHtml())
            else:
                convoManager.loadConversation(filenames[0],self.Ouput.toHtml(),loadMultiple=True)
            self.Ouput.clear()
            self.Ouput.setHtml(convoManager.getHTML())

    @Slot()        
    def resetView(self):
        self.setGeometry(500,500,750,750)
    
    @Slot()    
    def fullScreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
    @Slot()    
    def resetButton(self):
        self.Ouput.clear()
        convoManager.resetConvo()
        self.update_tokens(0)

    @Slot()    
    def addChat(self):
        self.toolBar_2.actions()[convoManager.getCurrentConversationID()].setChecked(False)
        convoManager.addConversation(self.Ouput.toHtml())
        action = QAction(QIcon(u"./Resources/chat_FILL1_24.svg"), "New chat", self)
        action.triggered.connect(self.changeChat)
        action.setCheckable(True)
        action.setChecked(True)
        action.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.toolBar_2.insertAction(self.toolBar_2.actions()[-6], action)
        self.Ouput.clear()

    @Slot()     
    def removeChat(self):
        for action in self.toolBar_2.actions():
            if action.isChecked():
                actionToRemove = action
        if actionToRemove.objectName() == 'actionchat': #the first chat -> do not delete
            self.Ouput.clear()
            convoManager.resetConvo()
        else:
            self.toolBar_2.removeAction(actionToRemove)
            self.Ouput.clear()
            convoManager.removeConversation()
            self.Ouput.setHtml(convoManager.getCurrentHTML())
            self.toolBar_2.actions()[convoManager.getCurrentConversationID()].setChecked(True) 

    @Slot()    
    def changeChat(self):
        self.toolBar_2.actions()[convoManager.getCurrentConversationID()].setChecked(False)
        sender = self.sender()
        for index, action in enumerate(self.toolBar_2.actions()):
            if action == sender:
                action.setChecked(True)
                chat = self.Ouput.toHtml()
                convoManager.changeConversation(index,chat)
                self.Ouput.clear()
                self.Ouput.setHtml(convoManager.getCurrentHTML())

    def _setColour(self):
        self.colour = QColorDialog.getColor(
                parent=self, options=QColorDialog.ColorDialogOption.DontUseNativeDialog
            )
        print(self.colour)
        self.changeColours(self.colour.name().strip('#'))


    def _setFont(self):
        ok,self.newFont = QFontDialog.getFont()
        self.Input.setFont(self.newFont)
        self.Ouput.setFont(self.newFont)

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
        # scrollbar = self.Ouput.verticalScrollBar()
        # cursor = self.Ouput.textCursor()
        # cursor.
        if self.scrollFollow:
            self.Ouput.ensureCursorVisible()
            self.Ouput.moveCursor(QtGui.QTextCursor.MoveOperation.End)
        self.Ouput.insertPlainText(result)

    #add specific token count
    def update_tokens(self,num):
        self.statusBar().showMessage(f"Tokens: {num}/4096")

    def startupSettings(self):
        settingsDict = config.settingsDict
        self.setGeometry(settingsDict['posx'],settingsDict['posy'],settingsDict['screenwidth'],settingsDict['screenheight'])
        qdarktheme.setup_theme(settingsDict['theme'])
        self.SVGcls = SVG(settingsDict['iconcolour'])
        self.changeColours(settingsDict['iconcolour'])
    
    
    # change this function to a for loop
    def changeColours(self, colour):
        self.SVGcls.changeColour(colour)

        icon_paths = {
            self.actionSettings: "./Resources/settings_FILL_24.svg",
            self.actionchat: "./Resources/chat_FILL1_24.svg",
            self.actionadd_chat: "./Resources/chat_add_on_FILL1_24.svg",
            self.actionOpen_chat: "./Resources/folder_open_FILL14.svg",
            self.actionSave: "./Resources/save_FILL1_24.svg",
            self.actionFont: "./Resources/font_download_FILL1_24.svg",
            self.actionDelete: "./Resources/delete_FILL1_24.svg"
        }
        for action, path in icon_paths.items():
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            action.setIcon(icon)     

    def closeEvent(self, event):
        # Perform any necessary saving or cleanup operations here
        settingsDict = {}
        geo = self.geometry()
        if self.isMaximized():
            diff = self.frameGeometry().height() - self.geometry().height()
            geoScreen = QGuiApplication.primaryScreen().availableGeometry()
            height = geoScreen.height() - diff
            width = geoScreen.width()
        else :
            height = geo.height()
            width =  geo.width()
        x = geo.x()
        y = geo.y()
        self.hide()
        settingsDict['screenwidth'] = str(width)
        settingsDict['screenheight'] = str(height)
        settingsDict['posx'] = str(x)
        settingsDict['posy'] = str(y)
        settingsDict['maximized'] = str(True)
        settingsDict['iconcolour'] = 'FFFFFF'
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
