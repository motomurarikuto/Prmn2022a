#!/usr/bin/env python3.5
#-- coding: utf-8 --

import RPi.GPIO as GPIO 
from pirc522 import RFID
import time


GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 

# ピン番号をLEDに割り当て
LED_RED1 = 3 
LED_GREEN = 5 

LED_RED2 = 11 
LED_ORANGE = 13 

LED_RED3 = 31 
LED_YELLOW = 33 

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

# りょうがのLED
# 退出のLED
def turn_red1_on () :
    turn_led_off(LED_GREEN) 
    turn_led_on(LED_RED1) 

# 入室のLED
def turn_green_on () :
    turn_led_off(LED_RED1) 
    turn_led_on(LED_GREEN)

def turn_red2_on () :
    turn_led_off(LED_ORANGE) 
    turn_led_on(LED_RED2)

def turn_orange_on () :
    turn_led_off(LED_RED2) 
    turn_led_on(LED_ORANGE)

def turn_red3_on () :
    turn_led_off(LED_YELLOW) 
    turn_led_on(LED_RED3)

def turn_yellow_on () :
    turn_led_off(LED_RED3) 
    turn_led_on(LED_YELLOW)


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
                Count_ryoga += 1
                if Count_ryoga % 2 == 1 :
                   turn_green_on()
                   print('りょうがが入室されました')
                else :
                   turn_red1_on()
                   print('りょうがが退出されました')
                    
            elif RFID_UID_rikuto == uid :
                Count_rikuto += 1
                if Count_rikuto % 2 == 1 :
                   turn_orange_on()
                   print('りくとが入室されました')
                else :
                   turn_red2_on()
                   print('りくとが退出されました')
            
            elif RFID_UID_yuya == uid :
                Count_yuya += 1
                if Count_yuya % 2 == 1 :
                   turn_yellow_on()
                   print('ゆうやが入室されました')
                else :
                   turn_red3_on()
                   print('ゆうやが退出されました')
                    
            elif RFID_UID_kyosuke == uid :
                Count_kyosuke += 1
                if Count_kyosuke % 2 == 1 :
                   turn_green_on()
                   print('きょうすけが入室されました')
                else :
                   turn_red_on()
                   print('きょうすけが退出されました')

            time.sleep(1) 

