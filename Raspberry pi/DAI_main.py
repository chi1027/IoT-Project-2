# DAI2.py #coding=utf-8 -- new version of Dummy Device DAI.py, modified by tsaiwn@cs.nctu.edu.tw
import time, DAN, requests, random 
import threading, sys # for using a Thread to read keyboard INPUT
import RPi.GPIO as GPIO
from take_pic import found, take
'''status = 0
pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin ,GPIO.IN)
'''
# ServerURL = 'http://Your_server_IP_or_DomainName:9999' #with no secure connection
#  注意你用的 IoTtalk 伺服器網址或 IP  #  https://goo.gl/6jtP41
ServerURL = 'https://4.iottalk.tw' # with SSL secure connection
# ServerURL = 'https://Your_DomainName' #with SSL connection  (IP can not be used with https)
Reg_addr = None #if None, Reg_addr = MAC address #(本來在 DAN.py 要這樣做 :-) 
# Note that Reg_addr 在以下三句會被換掉! # the mac_addr in DAN.py is NOT used
mac_addr = 'alicehuang'
# 若希望每次執行這程式都被認為同一個 Dummy_Device, 要把上列 mac_addr 寫死, 不要用亂數。
Reg_addr = mac_addr   # Note that the mac_addr generated in DAN.py always be the same cause using UUID !
DAN.profile['dm_name']='defender'   # you can change this but should also add the DM in server
DAN.profile['df_list']=['detect','Dummy_Weather']  # Check IoTtalk to see what IDF/ODF the DM has
DAN.profile['d_name']= 'who' # None
DAN.device_registration_with_retry(ServerURL, Reg_addr) 
print("dm_name is ", DAN.profile['dm_name']) ; print("Server is ", ServerURL)
# global gotInput, theInput, allDead    ## 主程式不必宣告 globel, 但寫了也 OK
gotInput=False
theInput="haha"
allDead=False

if __name__ == '__main__':
   while True:
      try:
         #Pull data from a device feature called "Dummy_Control"
         value1=DAN.pull('detect')
         if(value1 != None):  
            if(value1[0] == 1):          
               print('1')
               take()
               found()
               time.sleep(3)
         time.sleep(2)
      
         value2 = DAN.pull('Dummy_Weather')
         if value2 != None:
            weather = value2[0]
            f = open('a.txt', 'w')
            f.write(str(weather))
            f.close()
            print(value2[0])

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
   sys.exit( )