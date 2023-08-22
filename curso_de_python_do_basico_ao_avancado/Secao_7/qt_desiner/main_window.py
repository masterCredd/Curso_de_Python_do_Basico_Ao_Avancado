from PySide6.QtWidgets import QMainWindow, QApplication
from ndt_test import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        """
        The __init__ function is called when the class is instantiated.
        It sets up the user interface and connects signals to slots.

        :param self: Refer to the object itself
        :param parent: Pass a parent widget to the qwidget constructor
        :return: None
        :doc-author: Trelent
        """
        super().__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.changeLabelResult)

    def changeLabelResult(self):
        """
        The changeLabelResult function is called when the user clicks on the 
        button.
        It takes whatever text was entered in the lineName widget and sets it as 
        the labelResult widget's text.

        :param self: Represent the instance of the class
        :return: The text that was entered into the linename widget
        :doc-author: Trelent
        """
        text = self.lineName.text()
        self.labelResult.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
