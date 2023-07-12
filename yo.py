from PySide6.QtWidgets import QTextEdit, QMenu

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

class CodeTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def contextMenuEvent(self, event):
        menu = self.createStandardContextMenu()
        
        # Check if the selected text is within a code block
        cursor = self.cursorForPosition(event.pos())
        cursor.select(QTextEdit.document())
        selected_text = cursor.selectedText()
        
        if selected_text.startswith("'''") and selected_text.endswith("'''"):
            copy_action = QAction("Copy Code", self)
            copy_action.triggered.connect(self.copyCode)
            menu.addAction(copy_action)
        
        menu.exec_(event.globalPos())
    
    def copyCode(self):
        cursor = self.textCursor()
        cursor.select(QTextEdit.document())
        selected_text = cursor.selectedText()
        
        # Remove the ''' from the selected text
        code = selected_text[3:-3]
        
        # Copy the code to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(code)


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    
    text_edit = CodeTextEdit()

    
    window.setCentralWidget(text_edit)
    
    window.show()
    app.exec_()