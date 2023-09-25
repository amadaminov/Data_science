# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 15:37:16 2023

@author: admin
"""

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narhlar = [10000, 20000, 30000, 40000, 50000]
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = [] #bu bo'sh ro'yhat

#print('Birinchi meva', mevalar[0])
#print('Birinchi meva:', mevalar[0].title())
#print('Birinchi meva:', mevalar[0].upper())

#narhlar = [10000, 20000, 30000, 40000]
#print(narhlar[2] + narhlar[3])

#mevalar[2] = 'uzum' #element qiiymatini o'zgartirish
#print(mevalar)



#element qo'shish
#mevalar.append('banan') #append metodi ro'yhatning oxiriga qo'shadi
#print(mevalar)
#mevalar.insert(1, 'kiwi') #insert metodi xoxlagan joyga qo'shadi
#print(mevalar)


#elemnt o'chirish
#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
#del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
#print(mevalar)


#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
#mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
#print(mevalar)
# remove metodidan elementni indeksini bilamaganda foydalanamiz
#.remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi. Agar ro'yxatning ichida 2 va undan ko'p bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.

# Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)

