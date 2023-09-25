# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:22:54 2023

@author: admin
"""

#car = {"model" : "ferrari" , "rang":"qizil"}
#print(car["model"])
#print(car["rang"])

#en_uz = {"apple" : "olma" , "apricot" : "o'rik" }

#mevalar = {'olma':10000,'tarvuz':8000,'qovun':12000}
#print(f"Olma narhi {mevalar['olma']} so'm")

#talaba = {'ism':'murod olimov','yosh':20,'t_yil':2000}
#print(f"{talaba['ism'].title()},\
 #{talaba['t_yil']}-yilda tu'gilgan,\
 #{talaba['yosh']} yoshda")

#talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
#talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 


#talaba1 = {}
#talaba1["ism"] = "qobil rasulov"
#talaba1["kurs"] = 3
#talaba1["yosh"] = 20
#print(talaba1)
#print(f"Talaba {talaba1['ism'].title()} {talaba1['kurs']}-kurs")
#elementni yangilash
#talaba1["kurs"] = 4
#print(f"Talaba {talaba1['ism'].title()} {talaba1['kurs']}-kurs")

#lug'atdagi elementni del orqali o'chiriladi
#ya'ni del en_uz ["apple"]


telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
phone = telefonlar["ali"]
print(f"Alining telefoni {phone}")
#get() metodi lug'atning ichidagi birorbir elementni olish uchun ishlatiladi
phone = telefonlar.get("hasan", "Bunday ism mavjud emas")
print(phone)