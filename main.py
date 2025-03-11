import functions
import time
import webbrowser
import pyautogui


url = "https://elgoog.im/dinosaur-game/"
webbrowser.open(url)
time.sleep(5)
pyautogui.press('space')

functions.start_bot()
 