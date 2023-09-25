# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:27:14 2023

@author: admin
"""

#import math
#uzunlik = lambda pi, r : 2*pi*r
#print(uzunlik(math.pi,10))




#kvadrat = lambda x,y : x**y
#print(kvadrat(3,2))



#lambdaning ishlatilishi pastdagi kodda
#def daraja(n):
 #   return lambda x : x**n



#kvadrat = daraja(2)
#kub = daraja(3)
#print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")



#from math import sqrt 
#sonlar = list(range(11))
#ildizlar = list(map(sqrt, sonlar))
#print(ildizlar)




#sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
#def daraja2(x):
    #"""Berilgan sonning kvadratini qaytaruvchi funksiya"""
     #return x*x
#print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz




#sonlar = list(range(11))
#kvadratlar = list(map(lambda x:x*x,sonlar))
#print(kvadratlar)




#ikkita ro'yhatning elementlarini o'zaro qo'shish
#a = [4, 5, 6]
#b = [7, 8, 9]
#a_plus_b = list(map(lambda x,y:x+y,a,b))
#print(a_plus_b)



#import random as r
#sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
#juft_sonlar = list(filter(lambda son: son%2==0,sonlar))
#print(sonlar)
#print(juft_sonlar)



#mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
#mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
#print(mevalar_b)



#mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
#mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
#print(mevalar2)




mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(mevalar)




