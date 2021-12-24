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
cbtPos = [1555, 795], [1495, 795], [1435, 795], [1375, 795]
cbtHP = [1575, 800], [1515, 800], [1455, 800], [1395, 800]
f2bank = [1577, 167], [1577, 418], [1577, 561], [1196, 301], [1204, 309], [510, 413], [485, 404], [818, 810], [1008, 803], [912, 800], [1008, 802], [320, 455], [320, 455], [1417, 260]
b2inc = [647, 671], [328, 450], [1203, 407], [1220, 450]
inc2fish = [345, 743], [342, 600], [1200, 800], [1430, 780], [1577, 798], [1576, 691], [1570, 505], [1582, 454], [1103, 798], [1580, 455]
bankman = [1008, 348], [1055, 321], [1052, 377], [1101, 351], [1103, 397], [1151, 374]

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

def gotoBank():
    i = 0
    while i < len(f2bank):
        lclick(f2bank[i][0], f2bank[i][1])
        i += 1
        time.sleep(5)

def gotoInc():
    i = 0
    while i < len(b2inc):
        lclick(b2inc[i][0], b2inc[i][1])
        i += 1
        time.sleep(5)

def gotoFish():
    i = 0
    while i < len(inc2fish):
        lclick(inc2fish[i][0], inc2fish[i][1])
        i += 1
        time.sleep(5)

def checkOk():
    if pyautogui.locateOnScreen('ok.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) != None:
        lclick(960, 475)

def isded(x, y):
    if (pyautogui.pixel(x, y)[0] == 67) or (pyautogui.pixel(x, y)[0] == 68):
        return True
    else:
        return False

def isme(x, y):
    if (pyautogui.pixel(x, y)[2] == 0):
        return True
    else:
        return False

def attack():
    i = 0
    pyautogui.keyDown('2')
    time.sleep(np.random.uniform(0.1, 0.3))
    pyautogui.keyUp('2')
    time.sleep(np.random.uniform(0.5, 1.5))
    while isded(cbtPos[i][0], cbtPos[i][1]) == True:
        i += 1
    if isme(cbtHP[i][0], cbtHP[i][1]) == True:
        i += 1
    while isded(cbtPos[i][0], cbtPos[i][1]) == True:
        i += 1
    click(cbtPos[i][0], cbtPos[i][1])

def mve(l, r, way):
    if way == 0:
        lclick(left[l][0], left[l][1])
    else:
        lclick(right[r][0], right[r][1])

def combat():
    if pyautogui.locateOnScreen('pret.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) != None:
        way = 0
        l = 0
        r = 0
        lclick(606, 402)
        win32api.SetCursorPos((625, 400))
        time.sleep(1)
        if pyautogui.locateOnScreen('skrotum.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) == None:
            lclick(1053, 186)
            way = 1
        lclick(1525, 772)
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
                lclick(1174, 996)
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

def emptyInv():
    gotoBank()
    i = 0
    while pyautogui.locateOnScreen('consulter.png', region=(290,43,1337,996), confidence=0.9, grayscale=True) == None:
        rclick(bankman[i][0], bankman[i][1])
        i += 1
        time.sleep(0.4)
        if i == len(bankman):
            i = 0
    lclick(432, 480)
    time.sleep(1)
    lclick(1495, 260)
    pyautogui.keyDown('ctrl')
    for x in range(0, 20, 1):
        lclick(1306, 355)
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)
    lclick(1535, 261)
    pyautogui.keyDown('ctrl')
    for x in range(0, 40, 1):
        lclick(1306, 355)
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)
    pyautogui.keyDown('esc')
    time.sleep(0.2)
    pyautogui.keyUp('esc')
    gotoInc()
    gotoFish()
 
def isFull():
    lclick(1275, 850)
    time.sleep(1)
    if pyautogui.pixel(1192, 449)[1] == 102:
        lclick(1275, 850)
        emptyInv()
    else:
        lclick(1275, 850)

i = 0
while keyboard.is_pressed('q') == False:
    if i % 10 == 0:
        isFull()
    fish(inc1[i][0], inc1[i][1])
    i += 1
    if i == len(inc1):
        i = 0
