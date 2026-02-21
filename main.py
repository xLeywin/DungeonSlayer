import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    main_ui_file = QFile("ui/main_menu.ui")
    main_ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(main_ui_file)
    main_ui_file.close()

    window.setWindowIcon(QIcon("assets/icon.png"))
    window.setFixedSize(400, 520)

    # Set style
    with open("styles/dark_theme.css", "r") as f:
        style = f.read()
        window.setStyleSheet(style)

    window.show()
    app.exec()
