
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty, isNumOrDot
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):

    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    imputPressed = Signal(str)
    operatorPressed = Signal(str)

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
        """
        The keyPressEvent function is a function that allows the user to press 
        keys on their keyboard and have those key presses be recognized by the 
        program.
        The function takes in an event parameter, which is a QKeyEvent object. 
        The text of this event is stripped of any whitespace characters, 
        and then stored in 
        the variable 'text'. The key pressed by the user is also stored as 
        'key'. A list called KEYS stores all possible keys that can be pressed 
        on a keyboard. 
        A boolean value called 'isEnter' checks if the key pressed was either 
        enter or return (or =). A boolean value called 'isDelete'

        :param self: Represent the instance of the class
        :param event: QKeyEvent: Get the key that was pressed
        :return: None, so the function is not returning anything
        :doc-author: Trelent
        """
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,
            KEYS.Key_P
        ]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'

            self.operatorPressed.emit(text)
            return event.ignore()

        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.imputPressed.emit(text)
            return event.ignore()
