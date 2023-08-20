
import qdarktheme
from variables import (PRIMARY_COLOR, DARKER_PRIMARY_COLOR,
                       DARKEST_PRIMARY_COLOR)


qss = f"""
    QPushButton[cssClass="specialButton"]{{
        color:#fff;
        background:{PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover{{
        color:#fff;
        background:{DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed{{
        color:#fff;
        background:{DARKEST_PRIMARY_COLOR};
    }} 
"""


def setupTheme() -> None:
    """
    The setupTheme function is used to set the theme of the application.
        The function takes no arguments and returns nothing.
        It sets up a dark theme with rounded corners, using a custom primary 
        color (PRIMARY_COLOR).


    :return: A qss string
    :doc-author: Trelent
    """
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )
