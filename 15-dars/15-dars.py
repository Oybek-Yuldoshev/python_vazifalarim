# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:24:30 2021

@author: Admin
"""

# #N_1
# #python izohli lug'ati 2

# python = {'integer':'butun', 'float':'o\'nlik', 'if':'yoki', \
# 'print':'chop etmoq', 'title':'sarlavha', 'remove':'o\'chirmoq', \
# 'else':'yoki', 'in':'ichida', "for":'takrorlash', "upper":'kattalashtirish',\
# 'input':'kiritmoq', 'append':"qo'shmoq"}
# for k, v in sorted(python.items()):
#     print(f"{k} ning tarjimasi {v}")
    
# #N_2
# #davlatlar va poytaxtlar

# dav_poy = {"uzbekistan":"tashkent", "usa":"washington", \
#            'australia':'canberra',\
#            'kazakistan':'kazan',\
#            'tadjikistan':'dushanbe',\
#            "qirg'iziston":"bishkek",\
#         "geramnia":"berlin"}
# for d, p in sorted(dav_poy.items()):
#     print(f"{d.upper()} ning poytaxti {p.title()}!")

# #davlat alohida poytaxt alohida

# print("Davlatlar: \n")
# for d in sorted(dav_poy.keys()):
#     print(d.upper())
# print("Poytaxtlari: \n")
# for p in sorted(dav_poy.values()):
#     print(p.title())
    
# #N_3
# #poytaxt so'rang aytamiz

# dav_poy = {"uzbekistan":"tashkent", "usa":"washington", \
#            'australia':'canberra',\
#            'kazakistan':'kazan',\
#            'tadjikistan':'dushanbe',\
#            "qirg'iziston":"bishkek",\
#         "germnia":"berlin"}
# davlat = input("Iltimos, kerakli davlatni kiriting:\n").lower()
# poytaxt = dav_poy.get(davlat)
# if poytaxt==None:
#     print(f"Bizning bazamizda {davlat} haqida ma'lumot yo'q")
# else:
#     print(f"{davlat.upper()} ning poytaxti {poytaxt.title()}")

# #N_4
# #restoran menu
# menu = {'osh':15000, 'manti':10000, 'somsa':12000,\
#         'norin':14000, 'shorva':15000, 'shashlik':11000,\
#         'chuchvara':18000, 'lag\'mon':18000, 'shovla':15000,\
#         'mastava':10000, "moshxo'rda":14000}
# ichimliklar = {'ayron':5000, 'sharbat':3000, "qora  choy":2000,\
#                'ko\'k choy':2000}
# buyurtmalar=[]
# for n in range(3):
#     buyurtmalar.append(input('Iltimos, taom tanlang: ').lower())

# ichimlikla=[]
# for x in range(2):
#     ichimlikla.append(input('Iltimos, ichimlik tanlang: ').lower())
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"{taom.title()} {menu[taom]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {taom.title()} yo'q")
# for ichim in ichimlikla:
#     if ichim in ichimliklar:
#         print(f"{ichim.title()} {ichimliklar[ichim]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {ichim.title()} yo'q")    