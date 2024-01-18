import smbus
import time
import RPi.GPIO as GPIO 
from pirc522 import RFID
import time
from pandas import DataFrame

pinSum_A_21 = 0x00 #入力ピンの合計
pinSum_B_21 = 0xFF #退出ピンの合計

pinSum_A_22 = 0x00 #入力ピンの合計
pinSum_B_22 = 0xFF #退出ピンの合計

pinSum_A_23 = 0x00 #入力ピンの合計
pinSum_B_23 = 0xFF #退出ピンの合計


ID_name = {'ID':[ [122,106,75,50,105], [86,185,74,236,73], [148,25,186,2,53], [214,238,68,157,225],[132,49,166,2,17],[230,175,84,236,241] ],
          'Name':['涼雅', '陸斗', '勇哉', '恭佑','大輝','斗優'],
          'Enter_pin':[0x01, 0x02, 0x04, 0x08, 0x10, 0x20],
          'Count':[0, 0, 0, 0, 0, 0],
           'ICADDR':[0x21,0x22,0x23,0x21,0x22,0x23]
          }

id_name = DataFrame(ID_name)# ID_nameをデータフレームに変換

#設定
CHANNEL   = 1      # i2c割り当てチャンネル 1 or 0
REG_IODIR_A = 0x00   # 入出力設定レジスタA
REG_OLAT_A  = 0x14   # 出力レジスタA
REG_IODIR_B = 0x01   # 入出力設定レジスタB
REG_OLAT_B  = 0x15   # 出力レジスタB

bus = smbus.SMBus(CHANNEL) # チャネルの初期化

bus.write_byte_data(0x21, REG_IODIR_A, 0x00) # 入出力レジスタAの初期化
bus.write_byte_data(0x21, REG_IODIR_B, 0x00) # 入出力レジスタBの初期化
bus.write_byte_data(0x22, REG_IODIR_A, 0x00) # 入出力レジスタAの初期化
bus.write_byte_data(0x22, REG_IODIR_B, 0x00) # 入出力レジスタBの初期化
bus.write_byte_data(0x23, REG_IODIR_A, 0x00) # 入出力レジスタAの初期化
bus.write_byte_data(0x23, REG_IODIR_B, 0x00) # 入出力レジスタBの初期化

GPIO.setmode(GPIO.BOARD) # ラズパイのデジタルピンの初期化
GPIO.setwarnings(False) 


rc522 = RFID() # RFIDで読み取りの開始

bus.write_byte_data(0x21, REG_OLAT_A, pinSum_A_21) # 退出ピン(B)を全部光らせる
bus.write_byte_data(0x22, REG_OLAT_A, pinSum_A_22) # 退出ピン(B)を全部光らせる
bus.write_byte_data(0x23, REG_OLAT_A, pinSum_A_23) # 退出ピン(B)を全部光らせる

bus.write_byte_data(0x21, REG_OLAT_B, pinSum_B_21) # 退出ピン(B)を全部光らせる
bus.write_byte_data(0x22, REG_OLAT_B, pinSum_B_22) # 退出ピン(B)を全部光らせる
bus.write_byte_data(0x23, REG_OLAT_B, pinSum_B_23) # 退出ピン(B)を全部光らせる
          
print("学生証をかざしてください") 

while True:
    rc522.wait_for_tag() 
    (error, tag_type) = rc522.request() 

    if not error:
        (error, uid) = rc522.anticoll() 

        if not error: 
            result = id_name[id_name['ID'].apply(lambda x: set(uid).issubset(set(x)))] # id_nameとIDが一致した人の情報を格納

            id_name.loc[id_name['ID'].apply(lambda x: set(uid).issubset(set(x))), 'Count'] += 1 # Countを足している
            
            for index, row in result.iterrows():
                enter_pin = row['Enter_pin']
                if row['Count'] % 2 == 0: # 入室の処理
                          if row['ICADDR'] == 0x21:
                                    pinSum_A_21 += enter_pin # 入室ピンを足していく
                                    pinSum_B_21 -= enter_pin # 退出ピンを引いていく
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_A, pinSum_A_21) # 入室ピンを光らせる
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_B, pinSum_B_21) # 退出ピンを光らせる
                                    print(row['Name'] + 'が入室されました')
                          else if row['ICADDR'] == 0x22:
                                    pinSum_A_22 += enter_pin # 入室ピンを足していく
                                    pinSum_B_22 -= enter_pin # 退出ピンを引いていく
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_A, pinSum_A_22) # 入室ピンを光らせる
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_B, pinSum_B_22) # 退出ピンを光らせる
                                    print(row['Name'] + 'が入室されました')
                          else if row['ICADDR'] == 0x23:
                                    pinSum_A_23 += enter_pin # 入室ピンを足していく
                                    pinSum_B_23 -= enter_pin # 退出ピンを引いていく
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_A, pinSum_A_23) # 入室ピンを光らせる
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_B, pinSum_B_23) # 退出ピンを光らせる
                                    print(row['Name'] + 'が入室されました')
                else:
                          if row['ICADDR'] == 0x21:
                                    pinSum_A_21 -= enter_pin # 入室ピンを引いてい
                                    pinSum_B_21 += enter_pin # 退出ピンを足していく
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_A, pinSum_A_21) # 入室ピンを光らせる
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_B, pinSum_B_21) # 退出ピンを光らせる
                                    print(row['Name'] + 'が退出されました')
                           else if row['ICADDR'] == 0x22:
                                    pinSum_A_22 -= enter_pin # 入室ピンを引いてい
                                    pinSum_B_22 += enter_pin # 退出ピンを足していく
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_A, pinSum_A_22) # 入室ピンを光らせる
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_B, pinSum_B_22) # 退出ピンを光らせる
                                    print(row['Name'] + 'が退出されました')
                            else if row['ICADDR'] == 0x23:
                                    pinSum_A_23 -= enter_pin # 入室ピンを引いてい
                                    pinSum_B_23 += enter_pin # 退出ピンを足していく
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_A, pinSum_A_23) # 入室ピンを光らせる
                                    bus.write_byte_data(row['ICADDR'], REG_OLAT_B, pinSum_B_23) # 退出ピンを光らせる
                                    print(row['Name'] + 'が退出されました')
                  
            time.sleep(1)
