
from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import SMALL_FONT_SIZE


class Info(QLabel):

    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        """
        The __init__ function is called when the class is instantiated.
        It sets up the button with a text label and calls configStyle to set up
        the style of the button.

        :param self: Represent the instance of the class
        :param text: str: Set the text of the button
        :param parent: QWidget | None: Set the parent of the button
        :return: None
        :doc-author: Trelent
        """
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self) -> None:
        """
        The configStyle function sets the font size and alignment of the QLabel.

        :param self: Refer to the object itself
        :return: None
        :doc-author: Trelent
        """
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
