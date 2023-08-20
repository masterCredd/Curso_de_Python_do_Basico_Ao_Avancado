
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):

    def __init__(self, *args, **kwargs) -> None:
        """
        The __init__ function is called when the class is instantiated.
        It sets up the window, and configures it with a title bar.

        :param self: Represent the instance of the class
        :param *args: Send a non-keyworded variable length argument list to
        the function
        :param **kwargs: Pass a variable number of keyword arguments to the
        function
        :return: None
        :doc-author: Trelent
        """
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self) -> None:
        """
        The configStyle function sets the style of the QLabel object.
            It sets:
                - The font size to BIG_FONT_SIZE (defined in constants.py)
                - The maximum height to twice BIG_FONT_SIZE (so that it can
                fit two lines of text)
                - The maximum width to MINIMUM_WIDTH (defined in constants.py)
                so that it doesn't get too wide when displaying long numbers
                like pi or euler's number, and also so that it doesn't take
                up too much space on smaller screens like laptops or tablets.
                This is a tradeoff between

        :param self: Refer to the object itself
        :return: None, so the return value is none
        :doc-author: Trelent
        """
        margins = [TEXT_MARGIN for _ in range(4)]

        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMaximumHeight(BIG_FONT_SIZE * 2)
        self.setMaximumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        return super().keyPressEvent(event)
