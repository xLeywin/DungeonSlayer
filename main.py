import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    ui_file = QFile("ui/game_window.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    window.setWindowIcon(QIcon("assets/icon.png"))
    window.setFixedSize(400, 520)

    with open("styles/dark_theme.css", "r") as f:
        window.setStyleSheet(f.read())

    # get the stackedWidget
    stack = window.findChild(QWidget, "stackedWidget")

    # character page buttons
    # confirm_button = window.findChild(QWidget, "ConfirmButton")

    # Menu
    start_button = window.findChild(QWidget, "StartButton")
    exit_button = window.findChild(QWidget, "ExitButton")

    start_button.clicked.connect(lambda: stack.setCurrentIndex(1)) # go to character edit screen (1)
    exit_button.clicked.connect(app.quit)

    # Character Edit
    # confirm_button.clicked.connect(lambda: stack.setCurrentIndex(2))
    
    back_button = window.findChild(QWidget, "BackButton")
    back_button.clicked.connect(lambda: stack.setCurrentIndex(0))

    window.show()
    app.exec()