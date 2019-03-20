import time
import shutil
import RPi.GPIO as gpio
import os
import sys

#Einstellungen
klingel_gpio = 4 #GPIO, der mit der Schaltung verbunden ist
callfilepfad = "/home/pi/klingel.call" #Dateipfad in dem das Script die .call-Datei ablegt
sipkanal = "624" #Name des SIP-Kanals (in eckigen Klammern in der SIP.conf)
sipziel = "**9" #Ziel des Anrufes (Beispiel: **9 als Rundruf der Fritz!Box)
sipwartezeit = "2" #Wartezeit bevor wieder aufgelegt wird

###
#Hier wird die .call-Datei zusammengebaut und abgespeichert
callfile = "Channel: SIP/" + sipkanal + "/" + sipziel + "\nApplication: Playback\nWaitTime:" + sipwartezeit + "\nData: /var/lib/asterisk/sounds/custom/play"

cf = open(callfilepfad, "w")
cf.write(callfile)
cf.close()
###

gpio.setmode(gpio.BCM)
gpio.setup(klingel_gpio, gpio.IN, pull_up_down=gpio.PUD_UP)

def voip():
        try:
                shutil.copyfile(callfilepfad,'/var/spool/asterisk/outgoing/anruf.call')
		print(text)
        except Exception:
                pass

while True:
        time.sleep(0.01)
        if not gpio.input(klingel_gpio):
                time.sleep(0.1)
                if not gpio.input(klingel_gpio):
                        voip()
                        time.sleep(5)
