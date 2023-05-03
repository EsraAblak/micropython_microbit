from microbit import *
#display.scroll("Merhaba") kaydırarak yazdırır
#display.show("BTK") üstüne basar gibi yazdırır
#***************************************************
#display.show(Image.HAPPY)
#display.show(Image("09990:09000:09990:09000:09990")) E harfi
#display.show(Image("01110:01000:01110:01000:01110"))
#0-9 parlaklık gücü 1 en düşük 9 en yüksek
#***************************************************
#display.show(Image.HAPPY)
#sleep(1000)
#display.show(Image.SAD)
#sleep(1000)
#display.show(Image.YES)
#***************************************************
#display.show(Image.ASLEEP)
#sleep(1000)
#display.show(Image.SILLY)
#sleep(1000)
#display.show(Image.HAPPY)
#***************************************************
#display.show("i")
#sleep(1000)
#display.show(Image.HEART)
#sleep(1000)
#display.scroll("micro:bit")
#***************************************************
#yas=15
#display.show(yas)
#sehir="istanbul"
#display.scroll(sehir)
#***************************************************
#resim=[Image("00000:09090:00900:90009:09990"),
 #      Image("00000:09010:00900:90009:09990")]
#display.show(resim,loop=True,delay=500) delay->bekleme
#***************************************************
#resim1 = Image.HAPPY
#resim2 = Image.SAD

#display.show(resim1)
#sleep(1000)
#display.show(resim2)
#sleep(1000)
#display.clear()
#***************************************************
#display.scroll("my")
#display.show(Image.GIRAFFE)
#sleep(1000)
#display.scroll("is")
#display.show(Image("00000:09090:00000:90009:09990"))
#sleep(1000)
#display.clear()
#***************************************************
"""ucak=[Image("09000:09009:99999:09009:09000"),
     Image("90000:90090:99990:90090:90000"),
     Image("00000:00900:99900:00900:00000"),
     Image("00000:90000:90000:90000:00000"),
     Image("00000:00000:00000:00000:00000")]

display.show(ucak,loop=True,delay=500)"""
#***************************************************
"""display.set_pixel(0,0,9) 
->set_pixel ile hangi led üzerinde işlem yapmak istiyosak ona
göre koordinat değeri veriyoruz. 1. parametre x(sütun) 2.p(satır)
3.p parlaklık
sleep(1000)
display.set_pixel(2,2,9)
sleep(1000)
display.set_pixel(0,0,0)"""
#***************************************************
"""display.show(Image("00000:90099:00000:99009:99900"))
sleep(1000)
display.set_pixel(0,1,0)
sleep(1000)
display.set_pixel(4,1,0)
sleep(1000)
display.set_pixel(1,3,0)
sleep(1000)
display.set_pixel(0,4,0)
sleep(1000)
display.set_pixel(1,1,9)
sleep(1000)
display.set_pixel(3,4,9)"""
#***************************************************
"""sayi1=15
sayi2=17
toplam = sayi1+sayi2
display.scroll(toplam)"""
#***************************************************
"""adim=25
isim="ali"
adim = str(adim) ->string'e çevirir
display.scroll(isim+adim+"adim atmis")"""
#***************************************************
"""aliyas = "5"
ahmetyas = 4

aliyas = int(aliyas) ->integer'a çevirir
toplam = aliyas+ahmetyas
display.show(toplam)"""
