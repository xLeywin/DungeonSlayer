from PySide6.QtWidgets import QWidget

class CharacterCreation:

    def __init__(self, window, stack):

        self.window = window
        self.stack = stack

        ## Buttons
        play_button = self.window.findChild(QWidget, "PlayButton")
        back_button = self.window.findChild(QWidget, "BackButton")

        play_button.clicked.connect(self.start_game)
        back_button.clicked.connect(self.back_menu)
    
    def start_game(self):
        self.stack.setCurrentIndex(2)

    def back_menu(self):
        self.stack.setCurrentIndex(0)