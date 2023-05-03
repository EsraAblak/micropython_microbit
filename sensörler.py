from microbit import *

"""isikSeviyesi = 0
while True:
    isikSeviyesi = display.read_light_level()
    display.scroll(isikSeviyesi)"""

#microbit ışık okuma sensörü 0-255 derece arasında değer alır
#******************************************************

"""isikSeviyesi=0
while True:
    isikSeviyesi=display.read_light_level()
    if (isikSeviyesi<30):
        display.show(Image("00000:00000:00000:00000:04840"))
    elif (isikSeviyesi>30 and isikSeviyesi<80):
        display.show(Image("00000:00000:00000:44444:99999"))
    elif (isikSeviyesi>80 and isikSeviyesi<120):
        display.show(Image("00000:00000:44444:99999:99999"))
    elif (isikSeviyesi>120 and isikSeviyesi<170):
        display.show(Image("00000:44444:99999:99999:99999"))
    elif (isikSeviyesi>170 and isikSeviyesi<210):
        display.show(Image("44444:99999:99999:99999:99999"))
    elif (isikSeviyesi>210):
        display.show(Image("99999:99999:99999:99999:99999"))"""
#******************************************************
"""img = Image("11111:11111:11111:11111:11111")
while True:
    display.show(img * microphone.sound_level())"""
#******************************************************
"""while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HEART)
    elif microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.HEART_SMALL)"""
#******************************************************
"""while True:
    if accelerometer.was_gesture("shake"):
        sicaklik = temperature()
        display.scroll(sicaklik)"""
#******************************************************
#Pusula
"""compasscalibrate()
while True:
    aci = compass.heading()
    if (aci > 315 or aci < 45):
        display.show(Image.ARROW_N)
        sleep(500)
    elif (aci < 135):
        display.show(Image.ARROW_E)
        sleep(500)
    elif (aci < 225):
        display.show(Image.ARROW_S)
        sleep(500)
    else:
        display.show(Image.ARROW_W)
        sleep(500)
    if button_a.was_pressed():
        display.scroll(aci)"""
#******************************************************
#import speech

#speech.say("microbit")
#speech.pronounce("/HEHSEH4EH3EH2EH2EH3EH4EH5EHLP")
#speech.say("microbit",pitch=100,speed=120,mouth=200)
#******************************************************

import speech
from microbit import sleep

# The say method attempts to convert English into phonemes.
speech.say("I can sing!")
sleep(1000)
speech.say("Listen to me!")
sleep(1000)

# Clearing the throat requires the use of phonemes. Changing
# the pitch and speed also helps create the right effect.
speech.pronounce("AEAE/HAEMM", pitch=200, speed=100)  # Ahem
sleep(1000)

# Singing requires a phoneme with an annotated pitch for each syllable.
solfa = [
    "#115DOWWWWWW",   # Doh
    "#103REYYYYYY",   # Re
    "#94MIYYYYYY",    # Mi
    "#88FAOAOAOAOR",  # Fa
    "#78SOHWWWWW",    # Soh
    "#70LAOAOAOAOR",  # La
    "#62TIYYYYYY",    # Ti
    "#58DOWWWWWW",    # Doh
]

# Sing the scale ascending in pitch.
song = ''.join(solfa)
speech.sing(song, speed=100)
# Reverse the list of syllables.
solfa.reverse()
song = ''.join(solfa)
# Sing the scale descending in pitch.
speech.sing(song, speed=100)
    