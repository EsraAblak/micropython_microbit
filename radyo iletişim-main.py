from microbit import *
import radio

#Radyo Haberleşme
"""radio.config(group=7)
radio.on()

while True:

    gelenMesaj = radio.receive()
    if gelenMesaj:
        if (gelenMesaj == "duck"):
            display.show(Image.DUCK)
            sleep(500)
            display.clear()
        elif gelenMesaj=="snake":
            display.show(Image.SNAKE)
            sleep(500)
            display.clear()
    else:
        display.scroll("baglanti basarisiz")

    if (button_a.was_pressed()):
        radio.send("duck")
        display.show(Image.DUCK)
        sleep(500)
        display.clear()
    if (button_b.was_pressed()):
        radio.send("snake")
        display.show(Image.SNAKE)
        sleep(500)
        display.clear()"""

#*********************************************************
#Yön Belirleme
#radio.on()
#radio.config(channel=19)
#radio.config(power=7)

#gonderici kısım
"""while True:
    accX = accelerometer.get_x()
    if accX<-500:
        display.show(Image("00000:00000:09000:00000:00000"))
        sleep(500)
    elif accX>500:
        display.show(Image("00000:00000:00090:00000:00000"))
        sleep(500)
        
    radio.send(str(accX))"""

#alıcı kısım
"""while True:
    gelenVeri = radio.receive()
    if gelenVeri is not None:
        accX = int (gelenVeri)
        if (accX < -500):
            display.show(Image("00900:09000:99999:09000:00900"))
            sleep(500)
        elif (accX > 500):
            display.show(Image("00900:00090:99999:00090:00900"))
            sleep(500)
            """

#*********************************************************
#Send Arrow

radio.on()
radio.config(channel=19)
radio.config(power=7)

#gonderici kısım
"""while True:
    if (accelerometer.was_gesture("right")):
        radio.send("sag")
        display.show(Image.YES)
        sleep(500)
        display.clear()
    elif accelerometer.was_gesture("left"):
        radio.send("sol")
        display.show(Image.YES)
        sleep(500)
        display.clear()
    elif accelerometer.was_gesture("up"):
        radio.send("yukari")
        display.show(Image.YES)
        sleep(500)
        display.clear()
    elif accelerometer.was_gesture("down"):
        radio.send("asagi")
        display.show(Image.YES)
        sleep(500)
        display.clear()"""

#alıcı kısım
"""while True:
    gelenMesaj = radio.receive()
    if gelenMesaj:
        if gelenMesaj == "sag":
            display.show(Image.ARROW_E)
        elif gelenMesaj == "sol":
            display.show(Image.ARROW_W)
        elif gelenMesaj == "yukari":
            display.show(Image.ARROW_S)
        elif gelenMesaj == "asagi":
            display.show(Image.ARROW_N)"""
            
#*********************************************************
#How Fast

#gonderici mikrobit
"""while True:
    if (accelerometer.was_gesture("shake")):
        topaVurusAni = running_time()
        radio.send(str(topaVurusAni))
        display.show(Image.YES)
        """

#alici mikrobit
"""mesafe = 1000
while True:
    if accelerometer.was_gesture("shake"):
        topunGelisAni = running_time()
        display.show(Image.YES)
        topaVurusAni = radio.receive()

    if button_a.was_pressed():
        totalTime = (int(topunGelisAni) - int(topaVurusAni))/1000
        topunHizi = mesafe/totalTime
        display.scroll("V=")
        display.scroll(topunHizi)
        display.scroll("cm/s")"""

#*********************************************************
#Binary Puzzle

#gonderici
"""while True:
    if button_a.was_pressed():
        radio.send(str(1))
        display.show(1)
        sleep(500)
        display.clear()
    elif button_b.was_pressed():
        radio.send(str(0))
        display.show(0)
        sleep(500)
        display.clear()"""

#alici
"""x = 0
y = 0
while True:
    gelenVeri = radio.receive()
    
    if gelenVeri!=None:
        if y!=5:
            if gelenVeri=="1":
                display.set_pixel(x,y,9)
                
        if x!=5:
            x+=1
            
        if x==5:
            x=0
            if y!=5:
                y+=1"""
        
#*********************************************************
#Send Pixel

#gonderici
#display.show(Image.HEART)
"""while True:
    accx = accelerometer.get_x()
    accy = accelerometer.get_y()
    if (accx < -500 and accy < -500):
        for y in range(0,5):
            for x in range(0,5):
                if (display.get_pixel(x,y)!=0):
                    led = str(x)+str(y)
                    radio.send(led)
                    display.set_pixel(x,y,0)
                    sleep(1000)

    display.show(Image.YES)
    sleep(1000)
    display.clear()
    sleep(1000)"""

#alici
"""gelenX = 0
gelenY = 0
while True:
    gelenVeri = radio.receive()
    if gelenVeri != None:
        gelenX = int(gelenVeri[0])
        gelenY = int(gelenVeri[1])
        display.set_pixel(gelenX,gelenY,9)"""







