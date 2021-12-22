from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

inc1 = [908, 792], [909, 744], [855, 670], [765, 627], [768, 573], [766, 526], [813, 405], [862, 382], [958, 382], [1050, 429], [1100, 453], [1150, 479], [1244, 526], [1150, 576], [1150, 626], [1100, 700], [1100, 750], [1150, 770], [1575, 500], [1480, 450], [1385, 400], [1285, 350], [1200, 300], [1150, 285], [1385, 260], [1430, 285], [1475, 310]
left = [770, 332], [915, 269], [1055, 190]
right = [915, 260], [770, 340], [630, 405], [480, 480], [630, 555]


def checkOk():
    if pyautogui.locateOnScreen('ok.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) != None:
        click(960, 475)

def lclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def rclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def attack():
    pyautogui.keyDown('2')
    time.sleep(np.random.uniform(0.1, 0.3))
    pyautogui.keyUp('2')
    time.sleep(np.random.uniform(0.5, 1.5))
    if pyautogui.pixel(1575, 775)[2] == 255:
        click(1575, 775)
    else:
        click(1515, 775)

def mve(l, r, way):
    if way == 0:
        click(left[l][0], left[l][1])
    else:
        click(right[r][0], right[r][1])


def combat():
    way = 0
    l = 0
    r = 0
    if pyautogui.locateOnScreen('pret.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) != None:
        click(606, 402)
        win32api.SetCursorPos((625, 400))
        time.sleep(1)
        if pyautogui.locateOnScreen('skrotum.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) == None:
            click(1053, 186)
            way = 1
        click(1525, 772)
        time.sleep(10)
        while pyautogui.locateOnScreen('fermer.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) == None:
            if (way == 0) and (l < len(left)):
                mve(l, r, way)
                time.sleep(1.5)
                if pyautogui.locateOnScreen('skrotcbt.png', region=(290,43,1337,996), confidence=0.7, grayscale=True) != None:
                    l += 1
            elif (way == 1) and (r < len(right)):
                mve(l, r, way)
                time.sleep(1.5)
                if pyautogui.locateOnScreen('skrotcbt.png', region=(290,43,1337,996), confidence=0.7, grayscale=True) != None:
                    r += 1
            time.sleep(np.random.uniform(1, 1.6))
            attack()
            time.sleep(np.random.uniform(1, 1.6))
            attack()
            time.sleep(np.random.uniform(1, 1.6))
            attack()
            time.sleep(np.random.uniform(1, 1.6))
            if pyautogui.locateOnScreen('fermer.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) == None:
                click(1174, 996)
                time.sleep(np.random.uniform(7.3, 8.3))
        click(1381, 630)

#fermer X: 1381 Y:  629 RGB: (255, 255, 255)
#pret X: 1525 Y:  772 RGB: ( 38,  85, 167)
#cb X: 1549 Y:  775
#passer X: 1174 Y:  996 RGB: (255, 255, 255)



def fish(x, y):
    k = 10
    l = 70
    checkOk()
    combat()
    win32api.SetCursorPos((x, y))
    time.sleep(0.2)
    rclick(x, y)
    rclick(x, y)
    if pyautogui.locateOnScreen('pecher.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) != None:
        win32api.SetCursorPos((x+k,y+l))
        while pyautogui.pixel(x+k, y+l)[1] != 102:
            win32api.SetCursorPos((x+k, y+l))
            l -= 4
        lclick(x+k, y+l)
        time.sleep(np.random.uniform(19, 21))

i = 0
while keyboard.is_pressed('q') == False:
    fish(inc1[i][0], inc1[i][1])
    i += 1
    if i == len(inc1):
        i = 0
