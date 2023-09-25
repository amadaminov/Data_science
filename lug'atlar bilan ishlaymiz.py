# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:12:08 2023

@author: admin
"""

#.items
#talaba = {
 #   "ism" : "alion",
  #  "familya" : "shamshiyev",
   # "yosh" : 22,
    #"fakultet" : "matematika",
    #"kurs" : 4
    #}

#print(talaba.items())

#for kalit, qiymat in talaba.items():
 #   print(f"Kalit: {kalit}")
  #  print(f"Qiymat: {qiymat}")
  
#telefonlar = {
 #   "ali": "Iphone X",
  #  "vali": "Samsung Galaxy S9",
   # "Olim": "Redmi 9 pro"}

#for a, b in telefonlar.items():
 #   print(f"{a.title()}ning telefoni {b}")
 
#.keys()
#mahsulotlar = {
 #   "olma": 10000,
  #  "anor": 12000,
   # "uzum": 15000,
    #"anjir": 13000
    #}

#print(mahsulotlar.keys())

#print("Do'kondagi mahsulotlar:")
#for mahsulot in mahsulotlar:
 #   print(mahsulot.title())

#bozorlik = ['anor','uzum','non','baliq']
#for mahsulot in mahsulotlar:
 #   if mahsulot in bozorlik:
  #      print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#for buyum in bozorlik:
 #   if buyum not in mahsulotlar:
  #      print(f"Iltimos, do'koningizga {buyum} ham olib keling")
  
  #Lug'at elementlarini tartib bilan chiqarish
# print("Do'konimizdagi mahsulotlar:")    
#for mahsulot in sorted(mahsulotlar):
 #   print(mahsulot.title()) 
  

#Agar lug'atdagi qiymatlarni chiqarish talab qilinsa .values() metodidan foydalanishimiz mumkin.
#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
 #   print(tel)
 
 #set funksiyasi lug'atdagi takrorlangan elementlarning 1ta qilib chiqaradi
 #print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()):
 #   print(tel)
 
 
 