from microbit import *

"""def selamVer():
    display.scroll("Hi")

def sayiGoster():
    display.show(8)

while True:
    if (button_a.was_pressed()):
        selamVer()
    if (button_b.was_pressed()):
        sayiGoster()"""

#*******************************************************
#Hesap Makinesi

"""sayi=0
sonuc=0
islem=""

def Hesapla(sayiDegiskeni,islem):
    if (islem == "toplama"):
        sonuc=sayiDegiskeni+5
    elif (islem == "carpma"):
        sonuc = sayiDegiskeni*2

    display.clear()
    return (sonuc)

while True:
    if (button_a.was_pressed()):
        sayi += 1
        display.show(sayi)
    if (button_b.was_pressed()):
        sayi-=1
        display.show(sayi)
    if (accelerometer.was_gesture("left")):
        islem = "toplama"
        display.show(Image("00900:00900:99999:00900:00900"))
        sleep(500)
        display.scroll(Hesapla(sayi,islem))
    if (accelerometer.was_gesture("right")):
        islem = "carpma"
        display.show(Image("90009:09090:00900:09090:90009"))
        sleep(500)
        display.scroll(Hesapla(sayi,islem))"""

#*******************************************************
#Konfeti
import random

brightness=9
startTime=running_time()

while True:
    display.set_pixel(random.randint(0,4),random.randint(0,4),brightness)
    time = running_time()-startTime
    if (time>400):
        startTime=running_time()
        brightness=9
    if (brightness>0):
        brightness-=1
    sleep(90)
    



        





