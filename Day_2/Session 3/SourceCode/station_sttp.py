from pirc522 import RFID
import RPi.GPIO as GPIO
import time
from datetime import datetime
import pandas as pd
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

#data={'Users':[1]}
#df3 = pd.DataFrame(data)
df = pd.DataFrame(columns =['Users', 'Entry', 'Exit'])

#df = df.append(df3)
#print(df)

def station_data():
  print("Station entry")
  global df, entry, user_names, a
  start = time.time()

  while True:
    
    (error, tag_type) = rdr.request()
    if not error:
      print("Tag detected")
      (error, uid) = rdr.anticoll()
      if not error:
        uid1 = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])+str(uid[4])
        #print(user_names[uid1])
        a = user_names.get(uid1)
        now = datetime.now()
        
      if len(df[df.Users==a])==1:
          #print("Entry is noted")
          check_entry=df["Entry"][df.Users==a]
          check_exit = df['Exit'][df.Users==a]
          try:
              
              diff2 = now - check_exit[0]
              if diff2.seconds > 20:
                  #print("hello")
                  df = df[df.Users!=a]
                  data = {'Users':[a]}
                  df2 = pd.DataFrame(data)
                  df = df.append(df2)
                  df["Entry"][df.Users==a] = now
                  print(df)
                  print("Welcome User %s"%(str(a)))
                  entry += 1
                  station['userId'] = a
                  station['doorType'] = "Entry"
                  station['timeStamp'] = str(now)
                  station['stationName'] = "Vasai"

                  json_station = json.dumps(station)
                  myMQTTClient.publish("stationPolicy", json_station, 1)
              else:
                 
                 pass
          except:
               #print("Exit process")
               check_exit = df['Exit'][df.Users==a]
               if str(check_exit[0]) == b or str(check_exit[0]) == c or str(check_exit[0]) == d or str(check_exit[0]) == e:
                     entry_check = df["Entry"][df.Users==a]
                     diff = now - entry_check[0]
                     if diff.seconds > 5:      #stopping immediate exit after entry
                        #print("exiting")
                        entry = entry - 1
                        df["Exit"][df.Users==a] = now
                        station['userId'] = a
                        station['doorType'] = "Exit"
                        station['timeStamp'] = str(now)
                        station['stationName'] = "Andheri"

                        json_station = json.dumps(station)
                        myMQTTClient.publish("stationPolicy", json_station, 1)
                        print(df)
      else:
          #print("First time entry")
          data = {'Users':[a]}
          df2 = pd.DataFrame(data)
          df = df.append(df2)
          df["Entry"][df.Users==a] = now
          print(df)
          entry += 1
          station['userId'] = a
          station['doorType'] = "Entry"
          station['timeStamp'] = str(now)
          station['stationName'] = "Vasai"
          json_station = json.dumps(station)
          myMQTTClient.publish("stationPolicy", json_station, 1)
          
  return ((entry / 8 )* 100)

myMQTTClient = AWSIoTMQTTClient("station")
myMQTTClient.configureEndpoint("aa59isvlb0mnj.iot.ap-southeast-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("rootCA.pem", "26b447a44a-private.pem.key","26b447a44a-certificate.pem.crt")
myMQTTClient.connect()


station = {}
i = 0


GPIO.setwarnings(False)
rdr = RFID()

station = {}
user_names = {'645323413524': 115, '48241233135175': 116, '19348180171238': 109, '92220176171155': 108,
      '6423616124192': 107, '32148176171175': 110, '48154235135198': 111,
      '128117222135172': 112, '21953231171162': 113, '17212177171223': 105,
      '24023913421140': 114, '1285612613367': 106, '15022117617180': 104,
      '4223924810188':100, '8512912171115':101, '134889194219':102, '10177206101131':103,
      '0180128209':117}
b,c,d,e = 'NaT','NaN','nan', 'nat'
i, a = 0, 1

entry = 0.0

while True:
    entry_per = station_data()
    print("percentage :"+str(entry_per)+"%")
