from PySide6.QtCore import QEvent, QObject
import sys

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow, QApplication
from ndt_test import Ui_MainWindow
from typing import cast


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

        self.buttonSend.clicked.connect(self.changeLabelResult)  # type: ignore
        # self.labelName.setStyleSheet('background: red;')

        self.lineName.installEventFilter(self)

    def changeLabelResult(self):
        """
        The changeLabelResult function is called when the user clicks on the 
        button.
        It takes whatever text was entered in the lineName widget and sets it 
        as 
        the labelResult widget's text.

        :param self: Represent the instance of the class
        :return: The text that was entered into the linename widget
        :doc-author: Trelent
        """
        text = self.lineName.text()
        self.labelResult.setText(text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        """
        The eventFilter function is a reimplementation of the 
        QObject.eventFilter() function.
        It receives all events that are sent to watched objects and can process 
        them before they are delivered to the watched object.
        The eventFilter function returns True if it wants to stop further 
        processing of an event; otherwise, it returns False.

        :param self: Refer to the current object
        :param watched: QObject: Identify the object that is being watched
        :param event: QEvent: Get the type of event that has occurred
        :return: A boolean value
        :doc-author: Trelent
        """

        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.lineName.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
