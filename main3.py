import pyautogui as pg
import keyboard as kb

def vkladka(n):
    while n != 0:
        pg.moveTo(406, 51, a) #перемещаемся на первую вкладку
        pg.leftClick() #
        pg.moveTo(869, 864, a) #
        pg.leftClick() #
        kb.press_and_release('ctrl+v' )
        pg.typewrite(["Enter"])
        pg.moveTo(602, 43, a) #
        pg.leftClick()  #
        n -= 1
a = 1
vkladka(1)