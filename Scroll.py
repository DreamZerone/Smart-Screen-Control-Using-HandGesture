import pyautogui


def scroll_up_to_down():
    """
    Simulates scrolling from up to down in a presentation.

    This function simulates pressing the 'down' arrow key using PyAutoGUI.
    """
    pyautogui.scroll(-100)


def scroll_down_to_up():
    """
    Simulates scrolling from down to up in a presentation.

    This function simulates pressing the 'up' arrow key using PyAutoGUI.
    """
    pyautogui.scroll(100)
