from PySide6.QtWidgets import QWidget

class Menu:

    def __init__(self, window, stack):

        self.window = window
        self.stack = stack

        start_button = window.findChild(QWidget, "StartButton")
        exit_button = window.findChild(QWidget, "ExitButton")

        start_button.clicked.connect(self.open_character_creation)
        exit_button.clicked.connect(window.close)

    def open_character_creation(self):
        self.stack.setCurrentIndex(1)