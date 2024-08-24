import pyautogui
import time

time.sleep(10)
cnt = 50

while(cnt):
    # Press F2 key
    pyautogui.press('f2')

    # Press double quotation mark
    pyautogui.keyDown('shift')
    pyautogui.press("'")
    pyautogui.keyUp('shift')

    # Press Enter key
    pyautogui.press('enter')
    cnt = cnt-1
