import math
from typing import TYPE_CHECKING
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from utils import isNumOrDot, isEmpty, isValidNumber, converToNumber
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
        """
        The __init__ function is the first function called when you create a 
        new instance of a class.
        It's job is to initialize all of the attributes of an object.  In this 
        case, it initializes
        the display, info and window attributes with whatever values are passed 
        in as arguments.

        :param self: Store the instance of the class
        :param display: 'Display': Set the display variable to the value of 
        display
        :param info: 'Info': Pass the info object to the class
        :param window: 'MainWindow': Call the mainwindow class
        :param *args: Send a non-keyworded variable length argument list to 
        the function
        :param **kwargs: Pass keyworded, variable-length argument list
        :return: None
        :doc-author: Trelent
        """
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
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
    def equation(self, value) -> None:
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
        The _makeGrid function is responsible for creating the grid of buttons
            that will be displayed on the calculator. It also connects each 
            button to a slot function, which in turn calls _insertToDisplay 
            with the text of that button as an argument. The _makeGrid function 
            also configures special 
            buttons (i.e., those not representing numbers or decimal points) by 
            calling 
            self._configSpecialButton.

        :param self: Refer to the object that is calling the function
        :return: None
        :doc-author: Trelent
        """
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.imputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot) -> None:
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

    def _configSpecialButton(self, button: Button) -> None:
        """
        The _configSpecialButton function is a helper function that configures 
        the special buttons on the calculator.
        It takes in a button as an argument and then checks to see if it's text 
        matches any of the following: 'C', 'D', 'N', 
        '+-/*^' or '='. If it does, then it will connect that button to its 
        respective slot. For example, if we pass in a 
        button with text = &quot;C&quot;, then this function will connect that 
        button to self._clear(). The _configLeftOp() and _eq() functions are 
        also connected here.

        :param self: Refer to the object itself
        :param button: Get the text of the button
        :return: A function that takes in a button and returns a function
        :doc-author: Trelent
        """
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == 'D':
            self._connectButtonClicked(button, self.display.backspace)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text in '+-/*^':
            self._connectButtonClicked(
                button, self._makeSlot(self._configLeftOp, text)
            )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        """
        The _makeSlot function is a helper function that allows us to create 
        slots
        that can be connected to signals. The reason we need this function is 
        because
        we want the slot functions to have access to the self variable, which 
        they would
        not otherwise have if we just created them with lambda expressions. 
        This way, we can pass in any number of arguments and keyword arguments 
        into our slot 
        functions.

        :param self: Access the class attributes
        :param func: Pass the function that will be called when the button is 
        clicked
        :param *args: Pass a variable number of arguments to the function
        :param **kwargs: Pass keyword arguments to the function
        :return: A function that takes a boolean argument and returns nothing
        :doc-author: Trelent
        """
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self) -> None:
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = converToNumber(displayText) * -1
        self.display.setText(str(number))

    @Slot()
    def _insertToDisplay(self, text: str) -> None:
        """
        The _insertToDisplay function is a helper function that inserts text 
        into the display.
        It checks to see if the new value of the display is valid, and if it 
        isn't, it returns without doing anything.
        If it's valid, then we insert text into our display.

        :param self: Represent the instance of the class
        :param text: Insert the text into the display
        :return: Nothing
        :doc-author: Trelent
        """
        newDisplayValue = self.display.text() + text
        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self) -> None:
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
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, text: str) -> None:
        """
        The _configLeftOp function is responsible for configuring the left side 
        of the equation.
        It will also check if there is a valid number on the display, and if 
        not, it will show an error message.


        :param self: Represent the instance of the class
        :param text: Set the operation
        :return: The _left variable, which is the number on the left of the 
        operator
        :doc-author: Trelent
        """
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display
        self.display.setFocus()

        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Conta incompleta')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = converToNumber(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    @Slot()
    def _eq(self) -> None:
        """
        The _eq function is responsible for the following:
            1. It checks if the displayText is a valid number or not, and if 
            it isn't, it shows an error message.
            2. If there's no left value (self._left), then it also shows an 
            error message.
            3. It converts self._right to a float using converToNumber().
            4. The equation variable stores the string representation of our 
            math expression in infix notation (e.g., '2 + 3'). 
                This will be used later on to show what we calculated in our 
                info label widget at the bottom

        :param self: Represent the instance of the class
        :return: The result of the operation
        :doc-author: Trelent
        """
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('você o outro número da conta.')
            return

        self._right = converToNumber(displayText)
        # self._left: float
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'erro'

        try:

            if '^' in self.equation and isinstance(self._left, (int, float)):
                # result = eval(self.equation.replace('^', '**'))
                result = math.pow(self._left, self._right)
                result = converToNumber(str(result))
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
        self.display.setFocus()

        if result == 'erro':
            self._left = None

    @Slot()
    def _backspace(self) -> None:
        """
        The _backspace function is called when the backspace button is pressed.
        It calls the backspace function of the display widget, and then sets 
        focus to
        the display widget so that it can continue receiving keypresses.

        :param self: Represent the instance of the object itself
        :return: The backspace function
        :doc-author: Trelent
        """
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text: str):
        """
        The _makeDialog function is a helper function that creates a dialog box.
            It takes in one parameter, text, which is the message to be 
            displayed in the dialog box.

        :param self: Refer to the object itself
        :param text: Set the text of the message box
        :return: A message box object
        :doc-author: Trelent
        """
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text: str):
        """
        The _showError function is a helper function that displays an error 
        message to the user.
        It takes in one argument, text, which is the string of text that will be displayed to the user.
        The _showError function creates a QMessageBox object and sets its icon 
        to critical (a red circle with an X). 
        Then it executes this dialog box and returns focus back to the display.

        :param self: Access the attributes and methods of the class
        :param text: Display the error message
        :return: A message box with the text and an icon
        :doc-author: Trelent
        """
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text: str):
        """
        The _showInfo function is a helper function that creates a dialog box 
        with the given text.
        It sets the icon to an information icon and then executes it. It also 
        sets focus back on 
        the display.

        :param self: Refer to the instance of the class
        :param text: Display the text in the dialog box
        :return: A message box with the information icon
        :doc-author: Trelent
        """
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
