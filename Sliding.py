import pyautogui


def slide_left_to_right():
    """
    Simulates sliding from left to right in a presentation.

    This function simulates pressing the 'right' arrow key using PyAutoGUI.
    """
    pyautogui.press('right')


def slide_right_to_left():
    """
    Simulates sliding from right to left in a presentation.

    This function simulates pressing the 'left' arrow key using PyAutoGUI.
    """
    pyautogui.press('left')
