#!/usr/bin/env python3.5
#-- coding: utf-8 --

import RPi.GPIO as GPIO 
from pirc522 import RFID
import time


GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 

LED_RED = 3 
LED_GREEN = 5 

RFID_UID_ryoga = [122,106,75,50,105] #りょうがの学生証の番号
RFID_UID_rikuto = [86,185,74,236,73] #りくとの学生証の番号
RFID_UID_kyosuke = [214,238,68,157,225] #きょうすけの学生証の番号
RFID_UID_yuya = [148,25,186,2,53] #ゆうやの学生証の番号

Count_ryoga = 0
Count_rikuto = 0
Count_kyosuke = 0
Count_yuya = 0

def turn_led_on (led) :
    GPIO.setup(led, GPIO.OUT) 
    GPIO.output(led, GPIO.HIGH) 

def turn_led_off (led) :
    GPIO.setup(led, GPIO.OUT) 
    GPIO.output(led, GPIO.LOW) 


def turn_red_on () :
    turn_led_off(LED_GREEN) 
    turn_led_on(LED_RED) 

#Définit la fonction permettant d'allumer la verte et éteindre la rouge
def turn_green_on () :
    turn_led_off(LED_RED) #Eteind la led rouge
    turn_led_on(LED_GREEN) #Allume la led verte


rc522 = RFID() #On instancie la lib

print("En attente d'un badge (pour quitter, Ctrl + c): ") #On affiche un message demandant à l'utilisateur de passer son badge

#On va faire une boucle infinie pour lire en boucle
while True :
    rc522.wait_for_tag() #On attnd qu'une puce RFID passe à portée
    (error, tag_type) = rc522.request() #Quand une puce a été lue, on récupère ses infos

    if not error : #Si on a pas d'erreur
        (error, uid) = rc522.anticoll() #On nettoie les possibles collisions, ça arrive si plusieurs cartes passent en même temps

        if not error : #Si on a réussi à nettoyer
            if RFID_UID_ryoga == uid :
                Count_ryoga++
                if Count_ryoga%2 == 1 :
                   turn_green_on()
                   print('ryoga enter')
                else :
                   turn_red_on()
                   print('ryoga exit')
            else if RFID_UID_rikuto == uid :
                print('Badge {} autorisé !'.format(uid))
                turn_green_on()
            else if RFID_UID_yuya == uid :
                print('Badge {} autorisé !'.format(uid))
                turn_green_on()
            else if RFID_UID_kyosuke == uid :
                print('Badge {} autorisé !'.format(uid))
                turn_green_on()
            
            else :
                print('Badge {} interdit !'.format(uid))
                turn_red_on()

            time.sleep(1) #On attend 1 seconde pour ne pas lire le tag des centaines de fois en quelques milli-secondes

