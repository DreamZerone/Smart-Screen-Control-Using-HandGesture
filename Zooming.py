import pyautogui

zoom_size = 4


def zoom(axis_hands_pixel_difference):
    """
    Simulates zooming out on a presentation.

    This function moves the mouse cursor to the desired location to zoom out (adjust the coordinates based on your screen resolution).
    Then, it simulates pressing the Ctrl and '-' or '+' keys to zoom using PyAutoGUI.
    """
    # Simulate pressing the Ctrl and '+' keys to zoom out
    current_zoom_size = axis_hands_pixel_difference / 50
    global zoom_size

    # zooming out the window
    while zoom_size <= current_zoom_size:
        pyautogui.keyDown("ctrl")
        pyautogui.press("+")
        pyautogui.keyUp("ctrl")
        zoom_size += 1

    # zooming in the window
    while zoom_size >= current_zoom_size:
        pyautogui.keyDown("ctrl")
        pyautogui.press("-")
        pyautogui.keyUp("ctrl")
        zoom_size -= 1
