import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str) -> bool:
    """
    The isNumOrDot function takes a string as an argument and returns True if 
    the string contains only numbers or dots,
    and False otherwise. This function is used to determine whether a given 
    input is valid for the calculator.

    :param string: Check if the string is a number or dot
    :return: A boolean value
    :doc-author: Trelent
    """

    return bool(NUM_OR_DOT_REGEX.search(string))


def converToNumber(string: str):
    """
    The converToNumber function takes a string as an argument and returns the 
    number that is represented by the string.
    If the number is an integer, it will return an int; otherwise, it will 
    return a float.

    :param string: str: Define the type of data that will be passed into the 
    function
    :return: A float or an integer
    :doc-author: Trelent
    """
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number


def isValidNumber(string: str) -> bool:
    """
    The isValidNumber function takes a string as an argument and returns True 
    if the string can be converted to a float,
    and False otherwise. This function is used in the getValidNumber function 
    below.

    :param string: str: Pass in a string to the function
    :return: A boolean value
    :doc-author: Trelent
    """
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def isEmpty(string: str) -> bool:
    """
    The isEmpty function takes a string as an argument and returns True if 
    the string is empty, False otherwise.

    :param string: str: Specify the type of parameter that is being passed in
    :return: A boolean value
    :doc-author: Trelent
    """
    return len(string) == 0
