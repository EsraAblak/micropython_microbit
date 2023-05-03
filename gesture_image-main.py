from microbit import *
#***************************************************
#Gesture
"""while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.HEART)
    elif accelerometer.was_gesture("left"):
        display.show(Image.NO)
    elif accelerometer.was_gesture("up"):
        display.show(Image.YES)
    elif accelerometer.was_gesture("face down"):
        display.show(Image.SQUARE)"""
#was_gesture ile hangi hareketi yaptığını ölçüyosun
#*****************************************************
#Tas-Kagit-Makas

"""import random

#while True:
 #   if (accelerometer.was_gesture("shake")):
  #      rastgele = random.randint(0,2)
   #     if(rastgele == 0):
    #        display.show(Image.SQUARE)
     #   elif (rastgele==1):
      #      display.show(Image.SQUARE_SMALL)
       # elif (rastgele==2):
        #    display.show(Image.NO)

img = [Image.SQUARE,Image.SQUARE_SMALL,Image.NO]
while True:
    if accelerometer.was_gesture("shake"):
        rastgele = random.choice(img)
        display.show(rastgele)"""
#*****************************************************
#Accelerometer
            
"""while True:
    display.scroll(accelerometer.get_x())"""

#get_x ve get_y ile o eksende hareket derecene göre işlem
#*****************************************************
#Zürafa Geçidi

"""giraffe = Image.GIRAFFE
n = 0

while True:
    if accelerometer.get_x() < -500:
        n=n+1
        display.show(giraffe.shift_left(n))
        sleep(500)
        if (n == 5):
            n =- 5
    elif accelerometer.get_x() > 500:
        n = n+1
        display.show(giraffe.shift_right(n))
        sleep(500)
        if (n==5):
            n=-5"""

#get_x yerine was_gesture yapsaydın her hareketini tek tek alıcak
#tı get_x ile o yöne tuttuğunda devamlı olarak alır

#*****************************************************
#MicroBit müzik

"""import music

#while True:
 #   if (button_a.is_pressed()):
  #      music.play(music.CHASE)
   # elif button_b.is_pressed():
    #    music.play(music.BIRTHDAY)

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        audio.play(Sound.GIGGLE)
    elif button_b.is_pressed():
        display.show(Image.CONFUSED)
        audio.play(Sound.SPRING)"""
#*****************************************************
#Paso Kart
"""import music
bakiye=5
ulasimUcreti = 2

while True:
    if accelerometer.was_gesture("face down"):
        if (bakiye>ulasimUcreti):
            music.play(music.BA_DING)
            bakiye=bakiye-ulasimUcreti
            display.show(bakiye)
        else:
            music.play(music.WAWAWAWAA)
            display.show("YB")"""
#*****************************************************
#FizzBuzz

"""import music
for x in range(1,31):
    display.show(x)
    if button_a.was_pressed():
        if (x % 3 == 0 and x%5==0):
            display.scroll("fizzbuzz")
            music.play(music.JUMP_UP)
        elif (x % 3 == 0):
            display.scroll("fizz")
            music.play(music.JUMP_UP)
        elif (x % 5 == 0):
            display.scroll("buzz")
            music.play(music.JUMP_UP)
        else:
            display.show(Image.NO)
            music.play(music.BA_DING)
    sleep(500) """
#*****************************************************
#Zar
"""import random

while True:
    if accelerometer.was_gesture("shake"):
        for x in range(8):
            zar = random.randint(1,6)
            if zar == 1:
                display.show(Image("00000:00000:00900:00000:00000"))
            elif zar == 2:
                display.show(Image("00000:00090:00000:09000:00000"))
            elif zar == 3:
                display.show(Image("00000:00090:00900:09000:00000"))
            elif zar == 4:
                display.show(Image("00000:09090:00000:09090:00000"))
            elif zar == 5:
                display.show(Image("00000:09090:00900:09090:00000"))
            elif zar ==6:
                display.show(Image("00000:09090:09090:090909:00000"))
            sleep(100)
        """
#*****************************************************
#Kangaroo

"""import music
kangroo=Image("09009:99009:09990:00900:99000")
display.show(kangroo)

while True:
    if button_a.was_pressed():
        music.set_tempo(bpm=360) #->muzigin hızını ayarla
        music.play(music.JUMP_UP)
        for row in range(0,6):
            display.show(kangroo.shift_up(row))
            sleep(50)
        for row in reversed(range(0,6)):
            display.show(kangroo.shift_down(-row))# -> - yapmazsan
            #aşağıdan gelir gibi
            sleep(50)"""
#*****************************************************
#Reaksiyon
import music

while True:
    for x in range(0,5):
        display.set_pixel(x,2,9)
        sleep(30)
        display.set_pixel(x,2,0)
        sleep(30)
        if button_a.is_pressed():
            if x==3:
                display.clear()
                display.show(Image.HEART)
                audio.play(Sound.GIGGLE)
                sleep(200)
                display.clear()
            else:
                display.clear()
                display.show(Image.NO)
                audio.play(Sound.SAD)
                sleep(200)
                display.clear()

    for x in reversed(range(0,5)):
        display.set_pixel(x,2,9)
        sleep(30)
        display.set_pixel(x,2,0)
        sleep(30)
        if button_a.is_pressed():
            if x == 3:
                display.clear()
                display.show(Image.HAPPY)
                audio.play(Sound.GIGGLE)
                sleep(200)
                display.clear()
            else:
                display.clear()
                display.show(Image.NO)
                audio.play(Sound.SAD)
                sleep(200)
                display.clear()
                








