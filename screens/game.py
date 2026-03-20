from PySide6.QtWidgets import QLabel, QWidget, QScrollArea, QVBoxLayout
from PySide6.QtCore import QTimer, Qt

class Game:
    def __init__(self, window, stack):
        self.window = window
        self.stack = stack
        self.log_counter = 0

        self.scroll_area = self.window.findChild(QScrollArea, "ScrollArea")

        # QtDesigner has some limitations and so it was decided to scroll manually

        self.log_container = QWidget()
        self.layout_log = QVBoxLayout(self.log_container)
        self.layout_log.setAlignment(Qt.AlignTop)
        self.layout_log.setSpacing(2)
        self.layout_log.setContentsMargins(4, 4, 4, 4)

        self.scroll_area.setWidget(self.log_container)
        self.scroll_area.setWidgetResizable(True)

        self.timer = QTimer()
        self.timer.timeout.connect(self.add_event_log)
        self.timer.start(500)

    def add_event_log(self):
        self.log_counter += 1
        if self.layout_log:
            label = QLabel(f"> Event {self.log_counter:03d}")
            label.setStyleSheet("color: white; font-family: Consolas; font-size: 10px;")
            self.layout_log.addWidget(label)
            QTimer.singleShot(50, self.roll_bar_down)

    def roll_bar_down(self):
        bar = self.scroll_area.verticalScrollBar()
        bar.setValue(bar.maximum())