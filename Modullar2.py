# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:52:04 2023

@author: admin
"""

import avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz

avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
avto_info_mod.info_print(avto1)



import avto_info_mod as aim # avto_info_mod ni qisqa nom aim bilan chaqiramiz

avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
aim.info_print(avto1)





from avto_info_mod import avto_info, info_print
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)




from avto_info_mod import avto_info as ainfo, info_print as iprint
avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
iprint(avto1)




from avto_info_mod import *
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)





