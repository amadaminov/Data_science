# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 08:55:55 2023

@author: admin
"""
#09.08.2023 Chorshanba soat 10-11 orasi

#Tartiblash Sort
#cars = ['bmw', 'mercedes', 'volvo', 'audi', 'tesla']
#cars.sort()
#print(cars)
#Yuqoridagi list alifbo tarbida chiqaradi

#cars.sort(reverse=True)
#print(cars)
#Yuqoridagi kod alifboga teskari tartibda chiqaradi


#toq_sonlar = list(range(1,20,2))
#print('Toq_sonlar: ', toq_sonlar)
#juft_sonlar = list(range(2,20,2))
#print('Juft_sonlar: ', juft_sonlar)


#Min, Max, Summa
#narhlar = [5900,22600, 42900, 1500, 16000, 12000]
#arzon = min(narhlar)
#qimmat = max(narhlar)
#jami = sum(narhlar)
#print(min(narhlar))
#print(max(narhlar))
#print(sum(narhlar))
#print('Eng arzoni ', arzon, 'Xoni ', qimmat, 'Qiyamatinda ', jami)


cars = ['bmw', 'mercedes', 'volvo', 'audi', 'tesla']
#print(cars[0:3])
#print(cars[:4])
#print(cars[1:])
#my_cars = cars      # bir ro'yhatga 2 xil nom berilishi 
#my_cars.remove('tesla')
#print(my_cars)
#my_cars[1] = 'Nexia 3'
#print(my_cars)
# ro'yhatdan nusxa olish my_cars = cars[:] shu ko'rinishda bo'ladi


#tupple - bu o'zgarmas ro'yhat listdan farqi ro'yhatga element 
#qo'shib, o'chirib, yoki elementni almashtirib bo'lmaydi
#Agar mobodo ro'yhatni o'zgartirish zarur bo'lib qolsa 
#tupple ni oddiy listgs o'zgartirishimiz kk kodini keyingi qatorda qoldiraman
toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)




#Yuqoridagi kodni Alisher Madaminov yozdi