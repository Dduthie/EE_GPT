from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, QLabel
from PySide6.QtGui import QColor, QPainter
from PySide6.QtCore import Qt, Signal


class RectangleWidget(QWidget):
    clicked = Signal()
    def __init__(self, text):
        super().__init__()

        self.text = text
        self.selected = False

        # Set the background color
        # self.setStyleSheet("background-color: rgb(200, 200, 200);")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw a border around the widget if selected
        if self.selected:
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QColor("#0A67B0"))
            painter.drawRect(self.rect())

        # Draw the text in the center of the widget
        painter.setPen(Qt.GlobalColor.black)
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text)

    def mousePressEvent(self, event):
        self.selected = True
        self.update()
        self.clicked.emit()

    def deselect(self):
        self.selected = False
        self.update()

class PromptMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.resize(500,750)
        # Create a vertical layout for the menu
        layout = QVBoxLayout(central_widget)

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the rectangles
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)

        # Create a vertical layout for the rectangles
        scroll_layout = QVBoxLayout(scroll_widget)

        # Create rectangles as custom widgets
        self.rectangles:list[RectangleWidget] = []
        for i in range(10):
            rectangle = RectangleWidget(f"Rectangle {i+1}")
            rectangle.clicked.connect(self.rectangle_selected)
            scroll_layout.addWidget(rectangle)
            self.rectangles.append(rectangle)

        # Add the scroll area to the main layout
        layout.addWidget(scroll_area)

    def rectangle_selected(self):
        sender = self.sender()
        for rectangle in self.rectangles:
            if rectangle is not sender:
                rectangle.deselect()
        if sender.selected:
            print(f"Rectangle {sender.text} selected")
        else:
            print(f"Rectangle {sender.text} deselected")

if __name__ == "__main__":
    app = QApplication([])
    window = PromptMenu()
    window.show()
    app.exec()