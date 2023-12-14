import smbus
import time
import RPi.GPIO as GPIO 
from pirc522 import RFID
import time
from pandas import DataFrame

pinSum = 0x00 # エンターピンを足した値を代入

ID_name = {'ID':[[122,106,75,50,105],[86,185,74,236,73],[148,25,186,2,53]],
          'Name':['涼雅','陸斗','勇哉'],
          'Enter_pin':[0x08,0x28,0xA8],
          'Exist_pin':[3,11,31],
          'Count':[0,0,0]
          }

#設定
CHANNEL   = 1      # i2c割り当てチャンネル 1 or 0
ICADDR    = 0x20   # スレーブ側ICアドレス
REG_IODIR_A = 0x00   # 入出力設定レジスタA
REG_OLAT_A  = 0x14   # 出力レジスタA
REG_IODIR_B = 0x01   # 入出力設定レジスタB
REG_OLAT_B  = 0x15   # 出力レジスタB

bus = smbus.SMBus(CHANNEL)

GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 

id_name = DataFrame(ID_name)

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
                if row['Count'] % 2 == 0:
                  pinSum += id_name['Enter_pin']
                  bus.write_byte_data(ICADDR, REG_IODIR, pinSum)
                  print(row['Name'] + 'が入室されました')
                else:
                  bus.write_byte_data(ICADDR, REG_IODIR, pinSum - id_name['Enter_pin'])
                  print(row['Name'] + 'が退出されました')
                time.sleep(1)