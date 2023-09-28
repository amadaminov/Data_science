# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:46:00 2023

@author: admin
"""

#import datetime as dt 
#hozir = dt.datetime.now()
#print(hozir)
###sanani ajratob olish
#print(hozir.date())
### vaqtni ajratib olish
#print(hozir.time())


#bugun = dt.date.today()
#print(f"Bugungi sana: {bugun}")
#Yangi_yil = dt.date(2023,12,31)
#print(f"Yangi yil bayrami: {Yangi_yil}")


#bugun = dt.date.today()
#qurbonHayit = dt.date(2024, 7, 19)
#farq = qurbonHayit-bugun
#print(farq)
#print(f"Qurbon Hayitiga {farq.days} kun qoldi")



#hozir = dt.datetime.now()
#futbol = dt.datetime(2021, 6, 22, 23, 45, 00)
#farq= futbol-hozir
#sekundlar = farq.seconds
#minutlar = int(sekundlar/60)
#soatlar = int(minutlar/60)
#print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
#print(f"Futbol boshlanishiga {minutlar} minut qoldi")
#print(f"Futbol boshlanishiga {soatlar} soat qoldi")


#import math
#PI = math.pi
#print(PI)

#E = math.e
#print(f"e ning qiymati: {E}")

#math.sin(math.pi/2)
#math.cos(0)
#math.tan(PI)
#math.degrees(math.pi/2)
#math.radians(90)

#math.log(5)
#math.log10(100)

#x = 4.6
#print(math.ceil(x))
#print(math.floor(x))

#x = 81

# Kvadrat ildiz
#math.sqrt(x)

# Darajaga oshirish
#math.pow(x,3) # x ning kubi

#math.pow(x,5) # x ning 5-darajasi

#math.pow(x,1/3) # x dan kub ildiz


#from pprint import pprint
#import json
#filename = 'bemor.json'
#try:
#    with open(filename) as f:
 #    bemor = json.load(f)
#except FileNotFoundError:  
 #   pass 
#else:
  #  pprint(bemor)

#RegEx - ANDOZA YORDAMIDA MATN IZLASH
import re
#word1 = "темир"
#word2 = "томир"
#word3 = "тулпор"
#andoza = "^т...р"
#print(re.match(andoza, word1))
#print(re.match(andoza, word2))
#print(re.match(andoza, word3))


#from uzwords import words
#andoza = "^т...р$"
#matches = []
#try:
# for word in words:
 #   if re.match(andoza,word): 
  #      matches.append(word)
#except FileNotFoundError:
 #   pass
#else:
 #print(matches) 


# ihateregex.io sahifasidan esa loyihangiz uchun tayyor andozalarni topishingiz mumkin.

# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
#andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
#msg = "Yangi parol kiriting"
#msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
#msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

#while True:
 #   password = input(msg)
  #  if re.match(andoza,password):
   #     print("Maxfiy so'z qabul qilindi")
    #    break
    #else:
     #   print("Maxfiy so'z talabga javob bermadi")

































