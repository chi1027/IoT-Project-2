# DAI2.py #coding=utf-8 -- new version of Dummy Device DAI.py, modified by tsaiwn@cs.nctu.edu.tw
import time
import DAN
import requests
import random
import threading
import sys  # for using a Thread to read keyboard INPUT
from crawl_weather_V8 import crawler
# ServerURL = 'http://Your_server_IP_or_DomainName:9999' #with no secure connection
ServerURL = 'http://4.iottalk.tw:9999'  # with SSL secure connection

# ServerURL = 'https://Your_DomainName' #with SSL connection  (IP can not be used with https)
Reg_addr = None  # if None, Reg_addr = MAC address

# Note that Reg_addr 在以下三句會被換掉! # the mac_addr in DAN.py is NOT used
mac_addr = 'CD8600D38000'  # put here for easy to modify :-)
# 若希望每次執行這程式都被認為同一個 Dummy_Device, 要把上列 mac_addr 寫死, 不要用亂數。
# Note that the mac_addr generated in DAN.py always be the same cause using UUID !
Reg_addr = mac_addr
# you can change this but should also add the DM in server
DAN.profile['dm_name'] = 'weather_info'
DAN.profile['df_list'] = ['info']   # Check IoTtalk to see what IDF/ODF the DM has
DAN.profile['d_name'] = DAN.profile['dm_name']  # None
DAN.device_registration_with_retry(ServerURL, Reg_addr)
print("dm_name is ", DAN.profile['dm_name'])
print("Server is ", ServerURL)

allDead = False

while True:
    try:
        if(allDead):
            break

        # Pull data from a device feature called "Dummy_Control"

        # Push data to a device feature called "Dummy_Sensor"

        # value2=random.uniform(1, 10)    ## original Dummy_Device example

        table = crawler()
        msg = table["日期"][0] + "\t" + table["時間"][0] + "的天氣預報" + "\n天氣: " + table["天氣"][0] + "\n溫度: " + (table["溫度(°C)"][0]) + "\n體感溫度: " + (table["體感溫度(°C)"][0]) + "\n降雨機率: " + (table["降雨機率(%)"][0]) + "\n相對溼度: " + (table["相對溼度(%)"][0]) + "\n風級: " + (table["風級"][0]) + "\n風力: " + (table["風力 (m/s)"][0]) + "\n風向: " + (table["風向"][0]) + "\n舒適度: " + (table["舒適度"][0])
        DAN.push('info', msg)

        for i in range(60):
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                break

        if(allDead):
            break

    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)
    try:
        time.sleep(0.2)
    except KeyboardInterrupt:
        break
time.sleep(0.25)
try:
    DAN.deregister()    # 試著解除註冊
except Exception as e:
    print("===")
print("Bye ! --------------", flush=True)
sys.exit()