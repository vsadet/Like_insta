import pyautogui as pg
# import keyboard as kb
import time
import random
import datetime

def podpiska_like(n):
    pg.leftClick(740, 261, 0.5)  # обновляем фильтр
    pg.leftClick(1186, 177, 0.5)
    pg.leftClick(1186, 177, 4.5)
    while n != 0:
        pg.leftClick(794, 258, 1.5) # клик фильтр
        pg.leftClick(633, 537, 1.5) # очищаем фильтр
        pg.leftClick(596, 633, 1.5) # выбираем пустые ячейки
        pg.leftClick(750, 806, 1.5) # клик по ОК
        pg.leftClick(513, 290, 0.5) # клик на ячейку с ссылкой
        pg.middleClick(432, 331, 1.0) # клик по ссылке
        pg.leftClick(316, 17, 1.5) # клик по вкладке
        # первый заход
        pg.leftClick(596, 1013, 1.5) # клик по 1 фото
        pg.moveTo(891, 566, 1.0) # наводим на середину фото
        pg.leftClick()
        pg.leftClick()
        pg.leftClick(1497, 563, 1.5) # открыть след фото
        pg.moveTo(891, 566, 1.0)
        pg.leftClick()
        pg.leftClick()
        pg.leftClick(1497, 563, 1.5) # открыть след фото
        pg.moveTo(891, 566, 1.0)
        pg.leftClick()
        pg.leftClick()
        pg.leftClick(1885, 119, 1.5) # закрыть фото
        # второй заход
        pg.leftClick(504, 941, 1.5)  # клик по 1 фото
        pg.moveTo(891, 566, 1.0)  # наводим на середину фото
        pg.leftClick()
        pg.leftClick()
        pg.leftClick(1497, 563, 1.5)  # открыть след фото
        pg.moveTo(891, 566, 1.0)
        pg.leftClick()
        pg.leftClick()
        pg.leftClick(1497, 563, 1.5)  # открыть след фото
        pg.moveTo(891, 566, 1.0)
        pg.leftClick()
        pg.leftClick()
        pg.leftClick(1885, 119, 1.5)  # закрыть фото
        pg.moveTo(885, 198, 0.5) # смещение на подписку
        pg.leftClick()
        pg.leftClick(1033, 198, 0.2) # первый раз пытаемся подписаться
        pg.leftClick(1181, 198, 0.2) # второй раз пытаемся подписаться
        pg.leftClick(1329, 198, 0.2) # третий раз пытаемся подписаться
        pg.leftClick(421, 17, 0.5) # закрываем вкладку
        pg.leftClick(802, 289, 1.0) # вызываем меню на ячейке
        pg.leftClick(771, 309, 1.0) # выбираем ОТПИСАТЬСЯ
        n -= 1
    pg.leftClick(422, 21, 1.0)  # закрыть вкладку

def otpiska(n):
    pg.leftClick(513, 290, 0.5)  # клик на ячейку с ссылкой
    pg.middleClick(432, 331, 1.0)  # клик по ссылке
    pg.leftClick(316, 17, 1.0)  # клик по вкладке
    pg.leftClick(1457, 118, 1.0)  # клик в профиль
    while n / 5 != 0:
        pg.moveTo(1220, 257, 2.0)  # клик по подпискам
        pg.leftClick()
        for i in range(0, 150):
            pg.leftClick(1170, 770, 0.0001)  # клик по ВНИЗ
            i -= 1
        pg.leftClick(1087, 731, 1.0)  # отписаться от 1
        pg.leftClick(960, 652, 1.0)
        pg.leftClick(1091, 674, 1.0)  # отписаться от 2
        pg.leftClick(960, 652, 1.0)
        pg.leftClick(1086, 609, 1.0)  # отписаться от 3
        pg.leftClick(960, 652, 1.0)
        pg.leftClick(1104, 551, 1.0)  # отписаться от 4
        pg.leftClick(960, 652, 1.0)
        pg.leftClick(1089, 496, 1.0)  # отписаться от 5
        pg.leftClick(960, 652, 1.0)
        pg.leftClick(123, 70, 3.0) # клик обновить страницу
        n -= 5
    pg.leftClick(422, 21, 1.0)  # закрыть вкладку

def komments(n):
    pg.leftClick(740, 261, 0.5)  # обновляем фильтр
    pg.leftClick(1186, 177, 0.5)
    pg.leftClick()
    while n != 0:
        pg.leftClick(449, 1014, 0.5)  # клик вкладку КОММЕНТАРИЙ
        pg.leftClick(439, 266, 0.5) # клик на пустую ячейку
        pg.hotkey('Backspace')
        pg.leftClick(437, 306, 0.5)  # клик на ячейку с коментом
        kb.press_and_release('ctrl+c')  # копируем комент
        pg.leftClick(238, 1018, 0.5)  # клик на 1 вкладку
        pg.leftClick(794, 258, 0.5) # клик фильтр
        pg.leftClick(633, 537, 0.5) # очищаем фильтр
        pg.leftClick(612, 627, 0.5) # выбираем пустые ячейки
        pg.leftClick(750, 806, 0.5) # клик по ОК
        pg.leftClick(513, 290, 0.5) # клик на ячейку с ссылкой
        pg.middleClick(439, 311, 1.0) # клик по ссылке
        pg.leftClick(316, 17, 1.0) # клик по вкладке
        pg.leftClick(441, 798, 1.5) # клик по 1 фото
        pg.moveTo(1151, 870, 1.0) # наводим на поле ввода комента
        pg.leftClick()
        kb.press_and_release('ctrl+v')  # вставляем комент
        pg.leftClick(1407, 868, 1.5)  # публикуем коммент
        pg.leftClick(422, 21, 1.0)  # закрыть вкладку
        pg.leftClick(802, 289, 1.0) # вызываем меню на ячейке
        pg.leftClick(735, 369, 1.0) # выбираем КОММЕНТ
        n -= 1


def storis(n):
    pg.leftClick(513, 290, 0.5)  # клик на ячейку с ссылкой
    pg.middleClick(432, 331, 1.0)  # клик по ссылке
    pg.leftClick(316, 17, 2.0)  # клик по вкладке
    pg.leftClick(1264, 116, 3.0)  # клик в главную
    pg.leftClick(1091, 239, 1.0)  # проматать сторис 1
    pg.leftClick(1091, 239, 1.0)  # проматать сторис 2
    pg.leftClick(1027, 234, 2.0)  # клик в сторис
    while n != 0:
        pg.leftClick(1223, 604, 3.0)  # следующая сторис
        n -= 1
    pg.leftClick(422, 21, 1.0)  # закрыть вкладку


def like(n):
    pg.leftClick(740, 261, 0.5)  # обновляем фильтр
    pg.leftClick(1186, 177, 0.5)
    pg.leftClick(1186, 177, 4.5)
    while n != 0:
        pg.leftClick(794, 258, 1.5) # клик фильтр
        pg.leftClick(633, 537, 1.5) # очищаем фильтр
        pg.leftClick(596, 633, 1.5) # выбираем пустые ячейки
        pg.leftClick(750, 806, 1.5) # клик по ОК
        pg.leftClick(513, 290, 0.5) # клик на ячейку с ссылкой
        pg.middleClick(432, 331, 1.0) # клик по ссылке
        pg.leftClick(316, 17, 1.0) # клик по вкладке
        pg.leftClick(441, 798, 1.5) # клик по 1 фото
        pg.moveTo(891, 566, 1.0) # наводим на середину фото
        pg.leftClick()
        pg.leftClick()
        pg.leftClick(1497, 563, 1.5) # открыть след фото
        pg.moveTo(891, 566, 1.0)
        pg.leftClick()
        pg.leftClick()
        pg.leftClick(1885, 119, 1.5) # закрыть фото
        pg.leftClick(421, 17, 0.5) # закрываем вкладку
        pg.leftClick(802, 289, 1.0) # вызываем меню на ячейке
        pg.leftClick(771, 309, 1.0) # выбираем ОТПИСАТЬСЯ
        n -= 1
    pg.leftClick(422, 21, 1.0)  # закрыть вкладку


def like_lenta(n):
    pg.leftClick(513, 290, 0.5)  # клик на ячейку с ссылкой
    pg.middleClick(432, 331, 1.0)  # клик по ссылке
    pg.leftClick(316, 17, 2.0)  # клик по вкладке
    pg.leftClick(1264, 116, 3.0)  # клик в главную
    pg.moveTo(770, 414, 1.0)
    while n != 0:
        pg.leftClick()
        pg.leftClick()
        pg.scroll(-1000)
        n -= 1
        time.sleep(random.randint(0, 10))
    pg.leftClick(421, 17, 0.5)  # закрываем вкладку


# n = 24

# while n != 0:
    #for i in range(0, 1):
    # time.sleep(10)
    # program_time = time.time()
    # all_time = time.time()
    #otpiska(15)  # от скольких страниц отписаться (кратно 5)
    # podpiska_like(18) # сколько страниц пролайкать и подписаться
    #komments(2) # ставит из 5 только 1
    #like(30)
    #storis(30) # сколько сторис просмотреть
    #like_lenta(40)
    # n -= 1
    # print("Время программы %s минут" % (int(time.time() - program_time) / 60))
    # time.sleep(random.randint(0, 100) +  3600)
    # print("Время программы с задержкой %s минут" % (int(time.time() - all_time) / 60))
    # print(f'Еще {n} циклов')

subscriptions_per_hour = 5
time_slip = 3600 / subscriptions_per_hour
n = 0
print('Время сна:', time_slip / 60, 'минут')
print('Время начала:', datetime.datetime.now())
while True:
    time.sleep(5)
    podpiska_like(1)
    time.sleep(random.randint(0, 100) + time_slip)
    n += 1
    print(n)