#!/usr/bin/env python3.5
#-- coding: utf-8 --

import RPi.GPIO as GPIO 
from pirc522 import RFID
import time


GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 

# ピン番号をLEDに割り当て
LED_RED = 3 
LED_GREEN = 5 

# 学生証の識別番号
RFID_UID_ryoga = [122,106,75,50,105] #りょうがの学生証の番号
RFID_UID_rikuto = [86,185,74,236,73] #りくとの学生証の番号
RFID_UID_kyosuke = [214,238,68,157,225] #きょうすけの学生証の番号
RFID_UID_yuya = [148,25,186,2,53] #ゆうやの学生証の番号

# 学生証をかざした回数(最初は0で初期化)
Count_ryoga = 0
Count_rikuto = 0
Count_kyosuke = 0
Count_yuya = 0

# LEDのオン・オフを関数で定義
def turn_led_on (led) :
    GPIO.setup(led, GPIO.OUT) 
    GPIO.output(led, GPIO.HIGH) 

def turn_led_off (led) :
    GPIO.setup(led, GPIO.OUT) 
    GPIO.output(led, GPIO.LOW) 


def turn_red_on () :
    turn_led_off(LED_GREEN) 
    turn_led_on(LED_RED) 
    
def turn_green_on () :
    turn_led_off(LED_RED) 
    turn_led_on(LED_GREEN) 


rc522 = RFID() # RFIDで読み取りの開始

print("学生証をかざしてください") 

while True :
    rc522.wait_for_tag() 
    (error, tag_type) = rc522.request() 

    if not error : 
        (error, uid) = rc522.anticoll() 

        # 学生証が読み取れたときの処理
        if not error : 
            if RFID_UID_ryoga == uid :
                Count_ryoga++
                if Count_ryoga % 2 == 1 :
                   turn_green_on()
                   print('りょうがが入室されました')
                else :
                   turn_red_on()
                   print('りょうがが退出されました')
                    
            else if RFID_UID_rikuto == uid :
                Count_rikuto++
                if Count_rikuto % 2 == 1 :
                   turn_green_on()
                   print('りくとが入室されました')
                else :
                   turn_red_on()
                   print('りくとが退出されました')
            
            else if RFID_UID_yuya == uid :
                Count_yuya++
                if Count_yuya % 2 == 1 :
                   turn_green_on()
                   print('ゆうやが入室されました')
                else :
                   turn_red_on()
                   print('ゆうやが退出されました')
                    
            else if RFID_UID_kyosuke == uid :
                Count_kyosuke++
                if Count_kyosuke % 2 == 1 :
                   turn_green_on()
                   print('きょうすけが入室されました')
                else :
                   turn_red_on()
                   print('きょうすけが退出されました')

            time.sleep(1) 

