import sys


from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH


if __name__ == '__main__':
    # criando aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # info
    info = Info('sua conta')
    window.addWidgetToVLayout(info)

    # icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # display
    display = Display()
    window.addWidgetToVLayout(display)

    # # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
