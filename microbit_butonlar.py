from microbit import *
#***************************************************
"""
sleep(2000) ->was_pressed() çalışmadan önce basman gerekir
display.scroll(button_a.was_pressed()) ->sol köşedeki butona 
basınca true, basmazsan false çıktısı verir"""
#***************************************************
"""
sleep(1000)
display.scroll(button_a.is_pressed())komut tam işlendiği anda
basman lazım"""
#***************************************************
"""sleep(2000)
display.scroll(button_b.get_presses()) ->kaç kez bastığının
sayısını verir"""
#***************************************************
"""while(True):
    display.show(Image.HEART)
    sleep(500)
    display.clear()
    sleep(500)"""
#***************************************************
"""
dancingMan1=Image("00900:99999:00900:09990:90009")
dancingMan2=Image("00900:99900:00900:09990:09009")
dancingMan3=Image("00900:00999:00900:09990:90090")
dancingMan4=Image("00900:09990:09990:00900:09090")
dancingMan=[dancingMan1,dancingMan2,dancingMan3,dancingMan4]
while True:
    display.show(dancingMan,delay=200) """
#***************************************************
"""sayi=0
while sayi<10:
    display.show(sayi)
    sleep(300)
    sayi+=1"""
#***************************************************
"""for x in range(8):
    display.show(x)
    sleep(200)
    display.clear()
    sleep(200)"""

"""for x in range(5,8):
    display.show(x)
    sleep(200)
    display.clear()
    sleep(200)"""
    
"""for x in range(3,12,3):
    display.show(x)
    sleep(200)
    display.clear()
    sleep(200)"""

"""isim ="ali"
for harf in isim:
    display.show(harf)
    sleep(200)
    display.clear()
    sleep(200)"""
#***************************************************
"""
img=Image("00000:"
          "00000:"
          "00000:"
          "00000:"
          "00900")

#display.show(img)
#sleep(200)
#display.show(img.shift_up(4)) 
#shift_up() ->ledi yukarı kaydırır 
#(1)-> kaç birim istiyosan
#sleep(200)
#display.show(img.shift_right(2))
#burada img eski konumundan gider

display.show(img)
sleep(200)
img  = img.shift_up(4)
display.show(img) 
sleep(200)
display.show(img.shift_right(2))
"""
#***************************************************
"""img=Image("00000:"
          "00000:"
          "00000:"
          "00000:"
          "00900")
display.show(img)
sleep(200)
#for x in range(4):
#    img = img.shift_up(1)
#    display.show(img)
#    sleep(200)

while True:
    img = img.shift_up(1)
    display.show(img)
    sleep(200)

    img = img.shift_right(1)
    display.show(img)
    sleep(200)

    img = img.shift_down(1)
    display.show(img)
    sleep(200)

    img = img.shift_left(1)
    display.show(1)
    sleep(200) """
#***************************************************
"""mood="mutlu"
while True:
    if mood=="mutlu":
        display.show(Image.HAPPY)
        sleep(500)
        mood="ofkeli"
    elif mood=="ofkeli":
        display.show(Image.ANGRY)
        sleep(500)
        mood="mutsuz"
    else:
        display.show(Image.SAD)
        sleep(500)"""
#***************************************************
"""while True:
    if(button_a.was_pressed()):
        display.show(Image.HEART)
    elif (button_b.was_pressed()):
        display.show(Image.HEART_SMALL)"""
#***************************************************
"""while True:
    if (button_a.is_pressed() and button_b.is_pressed()):
        display.scroll("AB")
    elif (button_a.is_pressed()):
        display.scroll("A")
    elif (button_b.is_pressed()):
        display.scroll("B")
    sleep(100)"""
#***************************************************
"""while True:
    if (button_a.was_pressed()):
        display.show(3)
        sleep(300)
        display.show(2)
        sleep(300)
        display.show(1)
        sleep(300)
        display.show(0)
        sleep(300)
        display.show(Image.YES)"""
#***************************************************
"""while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break 
    else:
        display.show(Image.SAD)
display.clear()"""
#***************************************************
"""sayac = 0
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        sayac = 0
        display.show(sayac)
    elif button_a.was_pressed():
        sayac=sayac+1
        display.show(sayac)
    elif button_b.is_pressed():
        sayac=sayac-1
        display.show(sayac)
    sleep(100)"""

#is.pressed kullanırsan üzerine basılı tuttuğunda saymaya devam
#eder was.pressed kullanırsan basılı tutsanda tek bir sefer sayar
#***************************************************
"""adimsayisi = 0
adimuzunluk=50
mesafe = 0
display.show(Image.YES)
while True:
    if (button_a.was_pressed()):
        adimsayisi+=1
    if button_b.was_pressed():
        display.show(adimsayisi)
        sleep(500)
        mesafe = adimsayisi * adimuzunluk
        display.show(mesafe)
        display.scroll("cm")"""
#***************************************************
"""resim1 = Image("00000:00000:99999:00000:00000")
resim2 = Image("00009:00090:00900:09000:90000")
resim3 = Image("00900:00900:00900:00900:00900")
resim4 = Image("90000:09000:00900:00090:00009")
zaman = 1000
while True:
    if (button_a.was_pressed()):
        zaman = zaman-250
    elif (button_b.was_pressed()):
        zaman = zaman+250
    display.show(resim1)
    sleep(zaman)
    display.show(resim2)
    sleep(zaman)
    display.show(resim3)
    sleep(zaman)
    display.show(resim4)
    sleep(zaman)"""
#***************************************************
"""evet=0
hayir=0
display.scroll("A->EVET")
sleep(1000)
display.scroll("B->HAYIR")
while True:
    if (button_a.is_pressed() and button_b.is_pressed()):
        if (evet>hayir):
            display.scroll("e kazandi")
        elif (hayir>evet):
            display.scroll("h kazandi")
        else:
            display.scroll("berabere")
    elif (button_a.was_pressed()):
        evet+=1
        display.show(Image.YES)
        sleep(200)
        display.show("?")
    elif button_b.was_pressed():
        hayir+=1
        display.show(Image.NO)
        sleep(200)
        display.show("?")"""
#***************************************************
"""import random

#while True:
 #   rastgele = random.randrange(9)
  #  display.show(rastgele)
   # sleep(500)

#random.randint(0,9) ->9 dahil sayı üret
#random.randrange(9) ->9'a kadar sayı üret
        
hayvanlar = [Image.COW,Image.BUTTERFLY,Image.GIRAFFE,Image.DUCK,
            Image.RABBIT,Image.SNAKE]
while True:
    rastgele = random.choice(hayvanlar)
    display.show(rastgele)
    sleep(500)

#diziden rastgele eleman seçiceksen choice"""