# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:01:55 2021

@author: Oybek
"""
#N_3
#poytaxt so'rang aytamiz

dav_poy = {"uzbekistan":"tashkent", "usa":"washington", \
           'australia':'canberra',\
           'kazakistan':'kazan',\
           'tadjikistan':'dushanbe',\
           "qirg'iziston":"bishkek",\
        "germnia":"berlin"}
davlat = input("Iltimos, kerakli davlatni kiriting:\n").lower()
poytaxt = dav_poy.get(davlat)
if poytaxt==None:
    print(f"Bizning bazamizda {davlat} haqida ma'lumot yo'q")
else:
    print(f"{davlat.upper()} ning poytaxti {poytaxt.title()}")
