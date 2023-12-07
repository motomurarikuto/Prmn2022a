import smbus
import time

CHANNEL   = 1      # i2c割り当てチャンネル 1 or 0
ICADDR    = 0x20   # スレーブ側ICアドレス
REG_IODIR = 0x01   # 入出力設定レジスタ
REG_OLAT  = 0x15   # 出力レジスタ

bus = smbus.SMBus(CHANNEL)

# ピンの入出力設定
bus.write_byte_data(ICADDR, REG_IODIR, 0x00)

# GPA3, GPA5, GPA7 出力オン
bus.write_byte_data(ICADDR, REG_OLAT, 0x28)
time.sleep(5)
# GPA3, GPA5, GPA7 出力オフ
bus.write_byte_data(ICADDR, REG_OLAT, 0x00)
