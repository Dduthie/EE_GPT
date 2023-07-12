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
    QWidget,QFontDialog,QFileDialog,QColorDialog,QMessageBox)
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
        self.restoreButton.released.connect(self.restoreDefaults)

        self.themeCombo.currentTextChanged.connect(self.themeChanged)

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
        self.actionExport_as_txt.triggered.connect(self.exportTXT)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        spacer.objectName = 'spacer'
        self.toolBar_2.insertWidget(self.toolBar_2.actions()[-4],spacer)

    @Slot()
    def test(self):
        self.changeColours('000000')

    @Slot()
    def themeChanged(self,text:str):
        qdarktheme.setup_theme(theme=text.lower(),custom_colors={'primary':f"#{self.colour}"})
        self.settingsDict['theme'] = text.lower()
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
        screen = QGuiApplication.primaryScreen().availableGeometry()
        w = 750
        h = 750
        x= screen.width()/2 -w/2
        y= screen.height()/2 - h/2
        
        self.setGeometry(x,y,w,h)

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
        noHash = self.colour.name().strip('#')
        self.changeColours(noHash)
        self.settingsDict['iconcolour'] = noHash

    def _setFont(self):
        ok,self.theFont = QFontDialog.getFont()

        self.Input.setFont(self.theFont)
        self.Ouput.setFont(self.theFont)

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

    def restoreDefaults(self):
        self.resetView()
        qdarktheme.setup_theme(config.defaultDict['theme'])
        self.theFont.setFamily(config.defaultDict['fontfam'])
        self.theFont.setPointSizeF(config.defaultDict['fontsize'])
        self.Input.setFont(self.theFont)
        self.Ouput.setFont(self.theFont)   
        self.changeColours(config.defaultDict['iconcolour'])    
        pass
    
    def startupSettings(self):
        self.settingsDict = config.settingsDict
        self.setGeometry(self.settingsDict['posx'],self.settingsDict['posy'],self.settingsDict['screenwidth'],self.settingsDict['screenheight'])
        qdarktheme.setup_theme(self.settingsDict['theme'])
        self.SVGcls = SVG(self.settingsDict['iconcolour'])
        if bool(self.settingsDict['maximized']):
            self.showMaximized()
        self.colour = self.settingsDict['iconcolour']
        self.theFont = QFont()
        self.theFont.setFamily(self.settingsDict['fontfam'])
        self.theFont.setPointSizeF(self.settingsDict['fontsize'])
        self.Input.setFont(self.theFont)
        self.Ouput.setFont(self.theFont)

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
            self.actionDelete: "./Resources/delete_FILL1_24.svg",
            self.actionExport_as_txt: "./Resources/export_FILL_48.svg"
        }
        for action, path in icon_paths.items():
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            action.setIcon(icon)

        icon = QIcon()
        icon.addFile("./Resources/font_download_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fontbutton.setIcon(icon)
        icon = QIcon()
        icon.addFile("./Resources/palette_FILL1_48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.paletteButton.setIcon(icon)
        
        qdarktheme.setup_theme(self.settingsDict['theme'],custom_colors={'primary':f"#{colour}"})
        
    def exportTXT(self):
        filename = QFileDialog.getSaveFileName(self,
            "Save Chat", "/home/", "Chat Export (*.txt)")
        if filename[0]:
            export = convoManager.exportConvo()
            with open(filename[0],'w') as f:
                for line in export:
                    f.write(line)
        
    def closeEvent(self, event):
        # Perform any necessary saving or cleanup operations here
        self.settingsDict = {}
        geo = self.geometry()
        if self.isMaximized():
            diff = self.frameGeometry().height() - self.geometry().height()
            geoScreen = QGuiApplication.primaryScreen().availableGeometry()
            height = geoScreen.height() - diff
            width = geoScreen.width()
            maxmized = True
        else :
            maxmized = False
            height = geo.height()
            width =  geo.width()
        x = geo.x()
        y = geo.y()
        self.hide()
        
        self.Ouput.fontPointSize()
        
        font = self.Ouput.currentFont()
        
        self.settingsDict['screenwidth'] = str(width)
        self.settingsDict['screenheight'] = str(height)
        self.settingsDict['posx'] = str(x)
        self.settingsDict['posy'] = str(y)
        self.settingsDict['maximized'] = str(maxmized)
        self.settingsDict['iconcolour'] = 'FFFFFF'
        self.settingsDict['fontfam']= font.family()
        self.settingsDict['fontsize']= str(font.pointSizeF())
        config.setUserSettings(self.settingsDict)
        event.accept()

def loadKey():
    with open('license.key','r') as f:
        key = f.readline()
        return key
        

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "license.key")
    if not os.path.exists(file_path):
        appCheck = QApplication([])
        # Show a popup error message
        error_message = "No license file detected. Ask Darian for key."
        QMessageBox.critical(None, "Error", error_message)    
        sys.exit(1)
        
    key = loadKey()
    cwd = os.getcwd()
    bot = EEGPT(key)
    config = Configurator()
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.startupSettings()
    window.show()

    sys.exit(app.exec())