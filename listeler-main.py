from microbit import *

"""dizi=["zeynep","oguz","ali"]
display.scroll(dizi[1])
sleep(1000)

sayiDizisi=[1,2,3,4]
display.show(sayiDizisi[2]) """

#************************************************

"""kelime="merhaba"
kelime2="dunya"
sayilar="0123456789"
yeni = kelime + " " + kelime2
#display.scroll(yeni)

liste=[1,2,3,4,9,8,7]
liste2=[4,5,6]

liste.append(5)
#display.show(liste[7])

sesliHarfler=["a","e","i","o"]
sesliHarfler.append("u")
#display.show(sesliHarfler[4])
#display.show(sesliHarfler[0:5])

sesliHarfler.pop(1)
#display.show(sesliHarfler[0:4])

liste.sort()
for x in range(0,len(liste)):
    display.show(liste[x])
    sleep(500)

harfler=["a","z","e","s","k"]
harfler.sort()
display.show(harfler[0:6])
sleep(500)

for x in reversed(range(0,len(kelime))):
    display.show(kelime[x])
    sleep(500)"""

#************************************************
"""import random
ortalama=0
toplam=0
sayiListesi=[1,65,3,6,2,12]
rastgeleSayi=0

while True:
    if button_a.was_pressed():
        for value in sayiListesi:
            toplam+=value
        display.scroll("T=")
        display.scroll(toplam)
    if button_b.was_pressed():
        ortalama=toplam/len(sayiListesi)
        display.scroll("O=")
        display.scroll(ortalama)
    if accelerometer.was_gesture("shake"):
        for x in range(0,4):
            rastgeleSayi=random.randint(0,49)
            display.scroll(rastgeleSayi)
            sayiListesi.insert(x,rastgeleSayi)"""

#************************************************

"""hayvanlar=["as","ke","ko","go","ku","mu"]
evcil=[]
vahsi=[]

while True:
    while len(hayvanlar) > 0:
        display.scroll(hayvanlar[0])
        if button_a.was_pressed():
            evcil.append(hayvanlar[0])
            hayvanlar.pop(0)
            display.show(Image.YES)
            sleep(500)
        if button_b.was_pressed():
            vahsi.append(hayvanlar[0])
            hayvanlar.pop(0)
            display.show(Image.YES)
            sleep(500)
            
    if accelerometer.was_gesture("left"):
        for value in evcil:
            display.scroll(value)
    if accelerometer.was_gesture("right"):
        for value in vahsi:
            display.scroll(value)"""

#************************************************

morse_alphabet = {
    '.-': 'A',     '-...': 'B',   '-.-.': 'C', 
    '-..': 'D',    '.': 'E',      '..-.': 'F',
    '--.': 'G',    '....': 'H',   '..': 'I',
    '.---': 'J',   '-.-': 'K',    '.-..': 'L',
    '--': 'M',     '-.': 'N',     '---': 'O',
    '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
    '...': 'S',    '-': 'T',      '..-': 'U',
    '...-': 'V',   '.--': 'W',    '-..-': 'X',
    '-.--': 'Y',   '--..': 'Z', 
    '-----': '0',  '.----': '1',  '..---': '2',
    '...--': '3',  '....-': '4',  '.....': '5',
    '-....': '6',  '--...': '7',  '---..': '8',
    '----.': '9'
}
"""
sinyalMesaj=""
mesajMetni=""
harf=""

while True:
    if (button_a.was_pressed()):
        display.show(".")
        sleep(500)
        display.clear()
        sinyal = "."
        sinyalMesaj = sinyalMesaj+sinyal
    elif button_b.was_pressed():
        display.show("-")
        sleep(500)
        display.clear()
        sinyal="-"
        sinyalMesaj = sinyalMesaj+sinyal
    elif accelerometer.was_gesture("shake"):
        display.scroll(sinyalMesaj)
        harf=morse_alphabet[sinyalMesaj]
        display.scroll(harf)
        sleep(1000)
        mesajMetni=mesajMetni+harf
        display.clear()
        sinyal=""
        sinyalMesaj=""
    elif accelerometer.was_gesture("down"):
        display.clear()
        sleep(500)
        display.scroll(mesajMetni)"""
        
#************************************************

"""alfabe="abcdefghijklmnoprstuvwxyz"
harfSirasi=0
mesajHarfleri=""
sifreliMesajHarfleri=""

while True:
    accX = accelerometer.get_x()
    display.show(alfabe[harfSirasi])

    if accX < -800:
        if harfSirasi==0:
            harfSirasi=26
        harfSirasi-=1
        display.show(alfabe[harfSirasi])
        sleep(300)

    if accX > 800:
        if harfSirasi==26:
            harfSirasi=0
        harfSirasi+=1
        display.show(alfabe[harfSirasi])
        sleep(300)

    if button_a.was_pressed():
        kaydirmaDegeri = harfSirasi
        display.scroll(kaydirmaDegeri)
    elif button_b.was_pressed():
        mesajHarfleri = mesajHarfleri + alfabe[harfSirasi]
        sifreIndexi = harfSirasi+kaydirmaDegeri
        sifreliMesajHarfleri = sifreliMesajHarfleri + alfabe[sifreIndexi]    
        display.show(Image.YES)
        sleep(300)
        display.clear()
    if accelerometer.was_gesture("shake"):
        display.scroll(mesajHarfleri)
        sleep(1000)
        display.show(Image.ARROW_E)
        sleep(1000)
        display.scroll(sifreliMesajHarfleri)
        sleep(1000)
        harfSirasi = 0
        kaydirmaDegeri=0
        sifreIndexi=0
        sifreliMesajHarfleri=""
        mesajHarfleri="""""

#************************************************

#radio morse 

import music
import radio

mektup=Image("99999:99099:90909:90009:99999")
radio.on()
radio.config(channel=11)
sinyal=""
sinyalMesajı=""
harf=""
mesajMetni=""
#gonderici
while True:
    if button_a.was_pressed():
        sinyal="."
        display.show(Image("00000:00000:00900:00000:00000"))
        music.play("C:1")
        radio.send(sinyal)
        sleep(500)
        display.clear()

    elif button_b.was_pressed():
        sinyal="-"
        display.show("-")
        music.play("C:4")
        radio.send(sinyal)
        sleep(500)
        display.clear()

    elif accelerometer.was_gesture("shake"):
        radio.send("ok")
        display.show(Image.YES)
        music.play(music.BA_DING)
        sleep(500)
        display.clear()
    elif accelerometer.was_gesture("down"):
        radio.send("bitti")
        display.show(mektup)
        music.play(music.JUMP_UP)
        sleep(1000)
        for x in range(0,6):
            display.show(mektup.shift_right(x))
            sleep(200)
        sleep(500)
        display.clear()
        display.scroll(mesajMetni)
        mesajMetni=""

#alici        
while True:
    gelenMesaj = radio.receive()
    if gelenMesaj is not None:
        if gelenMesaj == "ok":
            display.show(Image.YES)
            music.play(music.BA_DING)
            sleep(500)

            harf=morse_alphabet.get(sinyalMesajı,Image.SAD)
            if (harf != Image.SAD):
                display.show(harf)
                sleep(1000)
                mesajMetni=mesajMetni+harf
            else:
                display.show(harf)
                sleep(1000)

        display.clear()
        sinyalSirasi=0
        sinyal=""
        sinyalMesajı=""
        if gelenMesaj==".":
            display.show(Image("00000:00000:00900:00000:00000"))
            music.play("C:1")
            sleep(300)
            display.clear()
            sinyal="."
            sinyalMesajı = sinyalMesajı + sinyal

        elif gelenMesaj=="-":
            display.show("-")
            music.play("C:4")
            sleep(300)
            display.clear()
            sinyal="-"
            sinyalMesajı = sinyalMesajı + sinyal
        elif gelenMesaj=="biti":
            display.show(mektup)
            music.play(music.JUMP_UP)
            sleep(1000)
            for x in range(0,6):
                display.show(mektup.shift_right(-x))
                sleep(200)
            sleep(300)
            display.scroll(mesajMetni)
            sinyalMesajı=""
            harf=""
            sinyal=""
    
