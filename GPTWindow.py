from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread, Signal)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform,QTextCursor,QSyntaxHighlighter, QTextCharFormat, QColor)
from PySide6 import QtGui
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QTextEdit,
    QWidget,QFontDialog)
from PySide6 import QtCore
from PySide6.QtGui import QKeyEvent
#  pyuic6 -o UImainwindow.py -x UImainwindow.ui   
import sys
from UImainwindow_ui import Ui_MainWindow
from EEGPT import EEGPT
import qdarktheme
import sys


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
        
        self._ui.action_open_font_dialog.triggered.connect(
            lambda: QFontDialog.getFont(
                QFont(), parent=self, options=QFontDialog.FontDialogOption.DontUseNativeDialog
            ))
    
    def eventFilter(self, obj:QTextEdit, event:QKeyEvent):
        if event.type() == QtCore.QEvent.Type.KeyPress and obj is self.Input:
            if ((event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter) and not event.modifiers() == QtCore.Qt.ShiftModifier) and self.Input.hasFocus():
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
                return True
        return super().eventFilter(obj,event)

    def handle_worker_result(self, result):
        scrollbar = self.Ouput.verticalScrollBar()
        if self.scrollFollow:
            self.Ouput.ensureCursorVisible()
            self.Ouput.moveCursor(QtGui.QTextCursor.End)

        self.Ouput.insertPlainText(result)

    def update_tokens(self,num):
        self.tokenLabel.setText(f"Tokens:\n{num}/4096")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    qdarktheme.setup_theme("auto",)
    #qdarktheme.setup_theme(custom_colors={"primary": "#DC7633"})
    
    window.show()
    bot = EEGPT()
    sys.exit(app.exec())
