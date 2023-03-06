import pyautogui
import time
(x,y)=pyautogui.size()
pyautogui.moveTo(x/2,y/2)
pyautogui.move(-50,50)
while 1:
    pyautogui.move(100,0)
    pyautogui.move(0,-100)
    pyautogui.move(-100,0)
    pyautogui.move(0,100)
    time.sleep(2)
    