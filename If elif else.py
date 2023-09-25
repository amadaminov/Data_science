# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:25:11 2023

@author: admin
"""

#yosh = int(input("Yoshingiz nechida ? "))
#if yosh  <=4:
 #   print("Sizga kirish bepul.")
#elif yosh <=12:
 #   print("Sizga kirish 5000 so'm")
#else:
 #   print("Sizga kirish 10000 so'm")
 
 
#yosh = int(input("Yoshingiz nechida ? "))
#if yosh  <=4:
#    narh = 0
#elif yosh <=12:
 #   narh = 5000
#else:
 #   narh = 10000
    
#print(f"Sizga kirish {narh} so'm")

#kun = ("dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba", "yakshanba")
#kun = input("Bugun nima kun?>>>")
#if kun.lower()=="shanba" or kun.lower()=="Yakshanba":
 #       print("Bugun dam olish kuni")
#else:
 #       print("Bugun ish kuni.")        
       
#kun = ("dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba", "yakshanba")        
#kun = input("Bugun nima kun?>>>")
#harorat = float(input("Havo harorati qanday?>>>"))

#if kun.lower()=="yakshanba" and harorat>=30:
 #    print("Cho'milgani ketdik!")
#elif kun.lower()=="yakshanba" and harorat<30:
 #    print("Uyda dam olamiz!")       
#elif kun.lower()=="dushanba"  or kun.lower()=="seshanba" or kun.lower()=="chorshanba" or kun.lower()=="payshanba" or kun.lower()=="juma" or kun.lower()=="shanba" and harorat>0: 
 #    print("Diyor bn abetlanib kn raysentrga boromiz")
  
#narh = 15000 # mijoz 15000 so'mga taom oldi.
#choy = True # mijoz choy ham oldi
#salat = False # mijoz salat olmadi

#if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
 #   narh = narh + 10000 # narhga 10000 so'm qo'shamiz
#elif choy or salat: # agar choy yoki salat olgan bo'lsa
 #   narh = narh + 5000 # narhga 5000 so'm qo'shamiz

#print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz


#narh = 15000 # mijoz 15 so'mga ovqat oldi
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy:   # agar choy olsa
 #   print("Mijoz choy oldi.")
  #  narh = narh + 3000
#if salat:  # agar salat olsa
 #   print("Mijoz salat oldi.")
  #  narh = narh + 5000
#if non:    # agar non olsa
 #   print("Mijoz non oldi.")
  #  narh = narh + 2000
#if kompot: # agar kompot olsa
 #   print("Mijoz kompot oldi.")
  #  narh = narh + 5000
#if assorti: # agar assorti olsa
 #   print("Mijoz assorti oldi.")
  #  narh = narh + 15000
    
#print(f"Jami {narh} so'm")


#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() in menu:
 #   print('Buyurtma qabul qilindi.')
#else:
 #   print('Afsuski bizda bunday ovqat yo\'q')
    
    
#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti", "shashlik"]

#for taom in buyurtmalar:
 #   if taom in menu:
  #      print(f"Menuda {taom} bor")
   # else:
    #    print(f"Kechirasiz, menuda {taom} yo'q")   


#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti", "shashlik"]

#if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
 #   for taom in buyurtmalar:
  #      if taom in menu:
   #         print(f"Menuda {taom} bor")
    #    else:
     #       print(f"Kechirasiz, menuda {taom} yo'q")
#else: # agar ro'yxat bo'sh bo'lsa
 #   print("Savatchangiz bo'sh!")
    
#son = float(input("Juft son kiriting: "))
#if son%2:
 #   print('Bu son juft emas.')
#else:
 #   print("Rahmat!")   
    
    
#yosh = int(input("Yoshingiz nechida?"))

#if yosh<=4 or yosh>=60:
 #   narh = 0;
#elif yosh < 18:
 #   narh = 10000
#else:
 #   narh = 20000
#print(f"Chipta {narh} so'm")


#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
 #   print(f"{x}={y}")
#elif x<y:
 #   print(f"{x}<{y}")
#else:
 #   print(f"{x}>{y}")
    
#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
 #              'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


#savat = []
#for n in range(5):
 #   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


#for mahsulot in savat:
 #   if mahsulot in mahsulotlar:
  #      print(f"Do'konimizda {mahsulot} bor")
  #  else:
   #     print(f"Do'konimizda {mahsulot} yo'q")
        
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
        
users = ['alisher','aziza','yasina','umar']

login = input("Yangi login tanlang: ")

if login.lower() in users:
    print('Login band, yangi login tanlang!')
else:
    print(f"Xush kelibsiz, {login.title()}!")        

if mavjud_emas:
 print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
  
  
son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):


        print(f"{son} soni {n} ga qoldiqsiz bo'linadi") 
  
  
            