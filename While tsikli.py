# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:48:42 2023

@author: admin
"""

# input
#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)
#yosh = int(yosh)
#height = input("Bo'yingiz necha metr? ")
#height = float(height)


#while
#son = 1 #son ga 1 qiymatini beramiz
#while son<=5:  #toki son 5 dan kichik yoki teng ekan....
 #  print(son, end=' ')
  # son = son + 1
 #son +=1 #songa 1 qo'shamiz
#print('Dastur tugadi')
 
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur. ")
#savol = "Istalgan son kiriting"
#savol +="(dasturdan chiqish uchun exit deb yozing): "
#qiymat = ' '
#while qiymat !='exit':
 #   qiymat = input(savol)
  #  if qiymat != 'exit':
   #     print(float(qiymat)**2)
#print("Dastur tugadi")        
 


#ishora
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
#    qiymat = input(savol)
 #   if qiymat == 'exit':
  #       ishora = False
   # else:
    #    print(float(qiymat)**2)
#print("Dastur tugadi")        



#break while
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True: # abadiy tsikl
 #   qiymat = input(savol)
  #  if qiymat == 'exit':
   #     break # tsiklni to'xtatish
    #else:
     #   print(float(qiymat)**2)
#print("Dastur tugadi")        
        
#break while
#sonlar = list(range(1,11))
#for son in sonlar: 
 #   if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
  #      break
   # print(f"{son} ning kvadrati {son**2} ga teng")

#break continue
#sonlar = list(range(1,11))
#for son in sonlar:
 #   if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
  #      continue
   # print(f"{son} ning kvadrati {son**2} ga teng")
    
#son = 0
#while son<10:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)
        
        
 # infinite loop
son = 0
while son<10:
    if son%2!=0:
        continue
    else:
        print(son)       
    
son = 1
while son>0: 
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)
