from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

def handle_application_closing():
    # Perform any necessary cleanup or save operations here
    print("Application is closing")

app = QApplication([])

# Create a main window
window = QMainWindow()

# Create a button to close the application
button = QPushButton("Close Application", window)
button.clicked.connect(app.quit)

# Connect the handle_application_closing function to the aboutToQuit signal
app.aboutToQuit.connect(handle_application_closing)

# Show the main window
window.show()

# Run the application event loop
app.exec()                   