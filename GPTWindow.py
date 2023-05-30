from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

from PySide6 import QtCore

from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform,QTextCursor)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QTextEdit,
    QWidget)

from PySide6.QtGui import QKeyEvent
#  pyuic6 -o UImainwindow.py -x UImainwindow.ui   
import sys
from UImainwindow_ui import Ui_MainWindow
from EEGPT import EEGPT
import qdarktheme
#sys.argv += ['-platform', 'windows:darkmode=2']




class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.Input.installEventFilter(self)
        
    def eventFilter(self, obj:QTextEdit, event:QKeyEvent):
        if event.type() == QtCore.QEvent.Type.KeyPress and obj is self.Input:
            print(event.key())
            
            if (event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter) and self.Input.hasFocus():
                print("enter_pressed")
                input_text = self.Input.toPlainText()
                self.Ouput.append('> '+input_text +'\n\n')
                self.Input.clear()
                QApplication.processEvents()
                response = bot.send_messages_stream(input_text)
                for chunk in response:
                    try:
                        res = chunk['choices'][0]['delta']['content']
                        self.Ouput.insertPlainText(res)
                    except KeyError:
                        pass  
                    QApplication.processEvents()
                
                #self.Ouput.append(response)
                return True
        return super().eventFilter(obj,event)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle('Fusion')
    #['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    window = Mainwindow()
    window.show()
    bot = EEGPT()
    qdarktheme.setup_theme()
    
    sys.exit(app.exec())
else:
    print("Script called as module -> new subprocess")