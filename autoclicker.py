#druk op 'z' om autoclicker te starten, druk op 'x' om autoclicker te stoppenz

import pyautogui #imports pyautogui
import keyboard #imports keyboard
import time


def autoclicker(): #declares the function
    while True: #makes a infinite loop 
        pyautogui. click()  #makes your mouse click
        if keyboard.is_pressed('x'): #detects if b is pressed
            break #if b is detected it breaks the loop




while True:
    if keyboard.is_pressed('z'):
        autoclicker()
