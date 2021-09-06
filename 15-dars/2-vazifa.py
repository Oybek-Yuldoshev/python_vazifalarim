# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 10:54:06 2021

@author: Oybek
"""
#N_2
#davlatlar va poytaxtlar

dav_poy = {"uzbekistan":"tashkent", "usa":"washington", \
           'australia':'canberra',\
           'kazakistan':'kazan',\
           'tadjikistan':'dushanbe',\
           "qirg'iziston":"bishkek",\
        "geramnia":"berlin"}
for d, p in sorted(dav_poy.items()):
    print(f"{d.upper()} ning poytaxti {p.title()}!")

#davlat alohida poytaxt alohida

print("Davlatlar: \n")
for d in sorted(dav_poy.keys()):
    print(d.upper())
print("Poytaxtlari: \n")
for p in sorted(dav_poy.values()):
    print(p.title())