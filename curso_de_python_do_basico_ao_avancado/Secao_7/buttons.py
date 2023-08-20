import math
from typing import TYPE_CHECKING
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from utils import isNumOrDot, isEmpty, isValidNumber
from variables import MEDIUM_FONT_SIZE


if TYPE_CHECKING:
    from display import Display
    from main_window import MainWindow
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        """
        The __init__ function is called when the class is instantiated.
        It sets up the window, and configures it with a title bar.

        :param self: Represent the instance of the class
        :param *args: Send a non-keyworded variable length argument list to the 
                        function
        :param **kwargs: Pass in keyword arguments to the function
        :return: The super() function
        :doc-author: Trelent
        """
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self) -> None:
        """
        The configStyle function sets the font size and minimum size of 
        the button.


        :param self: Refer to the object itself
        :return: Nothing
        :doc-author: Trelent
        """
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow',
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = None
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        """
        The equation function returns the equation of the line in 
        slope-intercept form.


        :param self: Represent the instance of the class
        :return: The value of the equation
        :doc-author: Trelent
        """
        return self._equation

    @equation.setter
    def equation(self, value):
        """
        The equation function is a setter function that sets the value of the 
        equation variable.
            It also updates the text in info to display what is currently being 
            typed.

        :param self: Represent the instance of the class
        :param value: Set the text of the info label
        :return: The value of the equation
        :doc-author: Trelent
        """
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self) -> None:
        """
        The _makeGrid function creates a grid of buttons and adds them to the calculator's layout.
        It also connects each button's clicked signal to the 
        _insertButtonTextToDisplay slot, which inserts
        the text from the button into the display when it is clicked.

        :param self: Refer to the instance of the class
        :return: None
        :doc-author: Trelent
        """
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        """
        The _connectButtonClicked function is a helper function that connects 
        the clicked signal of a button to a slot.


        :param self: Represent the instance of the class
        :param button: Connect the button to a slot
        :param slot: Connect the button to a function
        :return: The clicked signal
        :doc-author: Trelent
        """
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == 'D':
            self._connectButtonClicked(button, self.display.backspace)

        if text in '+-/*^':
            self._connectButtonClicked(
                button, self._makeSlot(self._operatorClicked, button)
            )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        """
        The _insertButtonTextToDisplay function takes a button as an argument 
        and inserts the text of that button into the display.
        It also checks to make sure that the new value is a valid number.

        :param self: Refer to the instance of the class
        :param button: Get the text of the button
        :return: None
        :doc-author: Trelent
        """
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self):
        """
        The _clear function is used to clear the calculator's display and reset
        the equation string. It also clears the left and right operands, as 
        well as the operator.

        :param self: Refer to the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()  # +-/* (etc...)
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Conta incompleta')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError('você o outro número da conta.')
            return

        self._right = float(displayText)
        # self._left: float
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'erro'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                # result = eval(self.equation.replace('^', '**'))
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero.')
        except OverflowError:
            self._showError('Essa conta não pode ser realizada')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'erro':
            self._left = None

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
