

from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self) -> None:
        """
        The adjustFixedSize function is a helper function that adjusts the size 
        of the window to fit its contents, and then sets it as fixed.
        This is useful for when you want to make sure your window doesn't get 
        resized by users.

        :param self: Represent the instance of the class
        :return: The fixed size of the window
        :doc-author: Trelent
        """
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget) -> None:
        """
        The addWidgetToVLayout function adds a widget to the vLayout.
            
        
        :param self: Represent the instance of the object
        :param widget: QWidget: Add a widget to the layout
        :return: None
        :doc-author: Trelent
        """
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        """
        The makeMsgBox function is a helper function that creates a 
        QMessageBox object.
            It takes no arguments and returns the QMessageBox object.
        
        :param self: Represent the instance of the class
        :return: A qmessagebox object
        :doc-author: Trelent
        """
        return QMessageBox(self)
