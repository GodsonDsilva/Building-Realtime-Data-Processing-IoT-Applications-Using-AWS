from pirc522 import RFID
import time
rdr = RFID()
usernames = list(range(100,118))
user = {}
'''
user={'645323413524': 115, '48241233135175': 116, '19348180171238': 109, '92220176171155': 108,
      '6423616124192': 107, '32148176171175': 110, '48154235135198': 111,
      '128117222135172': 112, '21953231171162': 113, '17212177171223': 105,
      '24023913421140': 114, '1285612613367': 106, '15022117617180': 104,
      '4223924810188':100, '8512912171115':101, '134889194219':102, '10177206101131':103,
      '0180128209':117}'''

while True:
  for i in usernames:
  #rdr.wait_for_tag()
      (error, tag_type) = rdr.request()
      if not error:
        print("Tag detected")
        (error, uid) = rdr.anticoll()
        #print(uid)
        id1 = "".join(map(str, uid))
        print(id1)
        if id1 not in user.keys() and i not in user.values():
          user[id1] = i
          print(user)
        #print(user[id1])
        #time.sleep(5)
        if not error:
          
          # Select Tag is required before Auth
          if not rdr.select_tag(uid):
            # Auth for block 10 (block 2 of sector 2) using default shipping key A
            if not rdr.card_auth(rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
              # This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            
              # Always stop crypto1 when done working
              rdr.stop_crypto()

# Calls GPIO cleanup
rdr.cleanup()
