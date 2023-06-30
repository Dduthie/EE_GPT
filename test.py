import pickle

dumpy = "You are a helpful assistant who gives clear and concise answers, you ask for clarification if needed. If you do not know the answer to something you say that you do not know."
# dumpy = "You are an extremely rude and bitter asshole and dont like to help out very much. You always talk back. you swear very often.You are at the same time very funny"
with open(f"Pstart.pkl", "wb") as file:
    pickle.dump(dumpy, file)

















# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# def handle_application_closing():
#     # Perform any necessary cleanup or save operations here
#     print("Application is closing")

# app = QApplication([])

# # Create a main window
# window = QMainWindow()

# # Create a button to close the application
# button = QPushButton("Close Application", window)
# button.clicked.connect(app.quit)

# # Connect the handle_application_closing function to the aboutToQuit signal
# app.aboutToQuit.connect(handle_application_closing)

# # Show the main window
# window.show()

# # Run the application event loop
# app.exec()                   






# # # from PyQt5.QtWidgets import QApplication, QTextEdit
# # # from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor, QFont

# # # app = QApplication([])

# # # text_edit = QTextEdit()
# # # text_edit.show()

# # # # Function to update the QTextEdit with new text
# # # def update_text(new_text):
# # #     # Get the current cursor position
# # #     cursor = text_edit.textCursor()
# # #     cursor.movePosition(QTextCursor.End)

# # #     # Set the formatting for the new text
# # #     char_format = QTextCharFormat()
# # #     char_format.setFont(QFont("Arial", 12))
# # #     char_format.setForeground(QColor(0, 0, 0))  # Black color

# # #     # Apply the formatting to the new text
# # #     cursor.setCharFormat(char_format)

# # #     # Append the new text to the QTextEdit
# # #     cursor.insertText(new_text)

# # #     # Scroll to the end of the QTextEdit to show the new text
# # #     text_edit.ensureCursorVisible()

# # # # Example usage
# # # update_text("Hello, ")
# # # update_text("world!")