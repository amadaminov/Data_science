# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:53:23 2023

@author: admin
"""

# bir narsa ichida boshqa narsani joylsh NESTING deb aytiladi
#malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
#for n in range(10):
 #   new_car = { # har bir yangi mashina uchun lug'at yaratamiz
  #      'model':'malibu',
   #     'rang':None, # rangi noaniq
    #    'yil':2020,
     #   'narh':None, # narhi belgilanmagan
      #  'km':0,
       # 'korobka':'avto'
        #}
#    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
 #   for malibu in malibus[:3]:
  #   malibu["rang"]="qizil"
   #  for malibu in malibus[3:6]:
    #   malibu['rang']='qora'
     
    #for malibu in malibus:
    # if malibu['korobka']=='avto':
     #   malibu['narh']=40000
    #else:
     #   malibu['narh']=35000
      #  for malibu in malibus:
       #  print(malibu)
       
       
#Lug'at ichida lug'at

#dasturchilar = {
 #   'ali':['python','c++'],
  #  'vali':['html','css','js'],
   # 'hasan':['php','sql'],
    #'husan':['python','php'],
    #'maryam':['c++','c#']
   # }

#for ism, tillar in dasturchilar.items():
 #   print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
  #  for til in tillar:
   #     print(til.upper())
        
#pastdagi bir qatorda chiqarish        
#for ism, tillar in dasturchilar.items():
 #   print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
  #  for til in tillar:
   #     print(f'{til.upper()} ', end='')
   
   

hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())



       