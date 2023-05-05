from microbit import *

"""while True:
    pin0.write_digital(1)
    sleep(500)
    pin0.write_digital(0)
    sleep(500)"""

#********************************************************
#BreadBoard
"""
while True:
    pin0.write_digital(1)
    sleep(500)
    pin1.write_digital(1)
    sleep(500)
    pin2.write_digital(1)
    sleep(500)

    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(0)
    sleep(500)

    pin2.write_digital(1)
    sleep(500)
    pin1.write_digital(1)
    sleep(500)
    pin0.write_digital(1)
    sleep(500)

    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(0)
    sleep(500)"""

#********************************************************
#Sokak Lambalari

"""while True:
    isikSeviyesi = display.read_light_level()
    if (isikSeviyesi > 30 and isikSeviyesi < 80):
        pin0.write_digital(1)
        pin1.write_digital(1)
        pin2.write_digital(1)
    elif isikSeviyesi>79 and isikSeviyesi<150:
        pin0.write_digital(1)
        pin1.write_digital(1)
        pin2.write_digital(0)
    elif isikSeviyesi>149 and isikSeviyesi<210:
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)
    elif isikSeviyesi>209:
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0) """

#********************************************************
#RGB Led

"""while True:
    sleep(500)
    if button_a.was_pressed() and button_b.was_pressed():
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)
    elif button_a.was_pressed():
        pin0.write_digital(0)
        pin1.write_digital(1)
        pin2.write_digital(0)
    elif button_b.was_pressed():
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(1)"""

#********************************************************
import random
"""r=0
g=0
b=0

while True:
    if accelerometer.get_x() > 500:
        r=r+10
        pin0.write_analog(r)
        sleep(100)
    elif accelerometer.get_x() < -500:
        g=g+10
        pin1.write_analog(g)
        sleep(100)
    elif accelerometer.get_y() < -200:
        b=b+10
        pin2.write_analog(b)
        sleep(100)
    elif accelerometer.get_y() > 200:
        r=r+random.randint(0,10)
        g=g+random.randint(0,2)
        b=b+random.randint(0,7)

        pin0.write_analog(r)
        pin1.write_analog(g)
        pin2.write_analog(b)
        sleep(100)
    else:
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0)
    sleep(200)"""
        
#********************************************************
#Push Button
"""import music
import speech

while True:
    if pin0.read_digital() == 1:
        display.show(Image.HEART)
        speech.say("microbit")
        sleep(500)
        audio.play(Sound.GIGGLE)
        sleep(500)
        display.clear()

    elif pin0.read_digital() == 0:
        display.show("!")
        sleep(500)
        display.clear()
        sleep(500)"""
        
#********************************************************
#Potansiyometre

"""img = Image.TRIANGLE
display.show(img)
while True:
    potOku = pin0.read_analog()
    shift = int(potOku/102)-5  #0-1023 aralığı
    display.show(img.shift_left(shift))"""

#********************************************************
#Servomotor
"""def map(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow)/(fromHigh-fromLow)+toLow
    
while True:
    #pin0.write_analog(30)
    #sleep(500)
    #pin0.write_analog(150)
    #sleep(1000)
    #pin0.write_analog(2000)

    analogOku = pin0.read_analog()
    mappedValue = int(map(analogOku,0,1023,1,180))
    pin0.write_analog(mappedValue)
"""

#********************************************************
#Joystick

"""ledX=2
ledY=2

while True:
    joyX=pin0.read_analog()
    joyY=pin1.read_analog()
    joyB=pin2.read_digital()

    if (joyX < 200):
        if ledX>0:
            display.set_pixel(ledX,ledY,0)
            ledX=ledX-1
    elif joyX>900:
        if ledX<4:
            display.set_pixel(ledX,ledY,0)
            ledX+=1

    if (joyY < 200):
        if ledY>0:
            display.set_pixel(ledX,ledY,0)
            ledY=ledY-1
    elif joyY>900:
        if ledY<4:
            display.set_pixel(ledX,ledY,0)
            ledY+=1
            
    sleep(200)
    display.set_pixel(ledX,ledY,9)"""

#********************************************************
#Neopiksel
"""import neopixel

neopix=neopixel.NeoPixel(pin0,24)

while True:
    for pixel in range(0,24):
        neopix[pixel]=(255,0,0)
        neopix.show()
        
        sleep(50)

    for pixel in reversed(range(0,24)):
        neopix[pixel]=(0,0,0)
        neopix.show()
        sleep(50)

    #neopix.clear()
    #sleep(500)"""

#********************************************************
import neopixel
"""
neopix = neopixel.NeoPixel(pin0,24)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
purple=(255,0,255)
yellow=(255,205,0)

def yak(renk):
    for pixel in range(0,24):
        neopix[pixel]=renk
    neopix.show()
    return        

while True:
    yak(red)
    sleep(1000)
    yak(green)
    sleep(1000)
    yak(blue)
    sleep(1000)
    yak(purple)
    sleep(1000)
    yak(yellow)
    sleep(1000)"""

#********************************************************

"""neopix = neopixel.NeoPixel(pin0,24)
red=(255,0,0)
yellow=(255,205,0)
black=(0,0,0)

def sinyal(bas,bit,renk):
    for pixel in range(bas,bit):
        neopix[pixel] = renk
    neopix.show()
    return

while True:
    if accelerometer.get_x() > 500:
        sinyal(0,13,yellow)
        sleep(500)
        sinyal(0,13,black)
        sleep(500)

    elif accelerometer.get_x() < -500:
        sinyal(13,24,red)
        sleep(500)
        sinyal(13,24,black)
        sleep(500)

    else:
        sinyal(0,0,black)"""

#********************************************************
#HCSR-04

import machine
import utime

def get_dist():
    pin0.write_digital(0)
    utime.sleep(2)
    pin0.write_digital(1)
    utime.sleep(10)
    pin0.write_digital(0)

    d=machine.time_pulse_us(pin1,1,11600)
    if d > 0:
        return d/58
    else:
        return d
pin1.set_pull(pin1.NO_PULL)
while True:
    if button_a.was_pressed():
        d = get_dist()
        display.scroll(d)
        sleep(150)
    sleep(20)
