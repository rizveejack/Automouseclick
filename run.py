import pyautogui
import random
from time import sleep

while True:
    position_x = random.randint(400,600)
    position_y = random.randint(400,600)
    time_to_sleep = random.randint(30,55)

    screen_size = pyautogui.moveTo(x=position_x,y=position_y)
    pyautogui.leftClick()
    print (position_x,position_y)
    sleep(time_to_sleep)
