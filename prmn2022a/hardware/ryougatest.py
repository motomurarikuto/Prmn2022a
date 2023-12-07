#!/usr/bin/env python3.5
#-- coding: utf-8 --

import RPi.GPIO as GPIO 
from pirc522 import RFID
import time


GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 

from pandas import DataFrame

ID_name = {'ID':[[122,106,75,50,105],[86,185,74,236,73],[148,25,186,2,53]],
          'Name':['涼雅','陸斗','勇哉'],
          'Enter_pin':[5,13,33],
           'Exist_pin':[3,11,31],
           'Count':[0,0,0]
          }

id_name = DataFrame(ID_name)

# LEDのオン・オフを関数で定義
def turn_led_on (led) :
    GPIO.setup(led, GPIO.OUT) 
    GPIO.output(led, GPIO.HIGH) 

def turn_led_off (led) :
    GPIO.setup(led, GPIO.OUT) 
    GPIO.output(led, GPIO.LOW) 


rc522 = RFID() # RFIDで読み取りの開始

for pin in id_name['Exist_pin']:
    turn_led_on(pin)
          
print("学生証をかざしてください") 



while True:
    rc522.wait_for_tag() 
    (error, tag_type) = rc522.request() 

    if not error:
        (error, uid) = rc522.anticoll() 

        if not error: 
            result = id_name[id_name['ID'].apply(lambda x: set(uid).issubset(set(x)))]

            id_name.loc[id_name['ID'].apply(lambda x: set(uid).issubset(set(x))), 'Count'] += 1
            
            for index, row in result.iterrows():
                if row['Count'] % 2 == 1:
                    turn_led_off(row['Exist_pin']) 
                    turn_led_on(row['Enter_pin'])
                    print(row['Name'] + 'が入室されました')
                else:
                    turn_led_off(row['Enter_pin']) 
                    turn_led_on(row['Exist_pin'])
                    print(row['Name'] + 'が退出されました')

                time.sleep(1)
