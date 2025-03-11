import pyautogui 
from PIL import ImageGrab # Tried using this, but proved too slow
import keyboard
import mss # Another screen capture, checked online, it was a bit faster apparently
import time
import numpy as np


def get_pixel(image, x, y):
    """Returns pixel value at x and y"""
    return image[y, x]


def jump():
    """Dino jump function"""
    pyautogui.keyDown("up")
    time.sleep(0.2)
    pyautogui.keyUp("up")


def duck():
    """Dino duck function"""
    pyautogui.keyDown("down")
    time.sleep(0.4)
    pyautogui.keyUp("down")


def start_bot():
    """Starts the bot"""
    # Set up the image capture (1920x1080)
    capture_size = {"top": 600, "left": 400, "width": 300, "height": 300}
    sct = mss.mss()

    # Calculate time
    jumping_time = 0
    last_jumping_time = 0
    current_jumping_time = 0
    last_interval_time = 0

    # Interval to search for obstacles
    y_search_1 = 200 # For tall Cacti
    y_search_2 = 150 # For short Cacti
    y_search_bird = 110 # For birds
    x_start = 45
    x_end = 60
    max_x_end = 200

    # 3 seconds to switch to Chrome
    time.sleep(3)
    while True:
        if keyboard.is_pressed("q"):
            break

        # Grab image and turn into array
        screenshot = sct.grab(capture_size)
        # Turns image into np array, The 3 stands for RGB value counts
        np_image = np.array(screenshot)[:, :, :3]

        # Grabs the background color of the image
        background_color = get_pixel(np_image, 100, 100)

        # We scan each pixel in the desired range, reversed to start from the back
        for i in reversed(range(x_start, x_end)):
            # Checks if the pixel is not equal to the background_color
            if not np.array_equal(get_pixel(np_image, i, y_search_1), background_color) or \
               not np.array_equal(get_pixel(np_image, i, y_search_2), background_color):
                jump()
                jumping_time = time.time()
                current_jumping_time = jumping_time
                break
            if not np.array_equal(get_pixel(np_image, i, y_search_bird), background_color):
                duck()
                break
        

        # Speed up mechanism
        interval_time = current_jumping_time - last_jumping_time

        if last_interval_time != 0 and abs(interval_time - last_interval_time) > 0.5:  # Buffer to avoid over-compensating
            if interval_time < last_interval_time:  # Speeding up (interval decreasing)
                x_end += 5  # Increase search range
                if x_end >= max_x_end:
                    x_end = max_x_end

        last_jumping_time = jumping_time
        last_interval_time = interval_time
