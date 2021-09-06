# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:28:50 2021

@author: Oybek
"""
#N_4
menu = {'osh':15000, 'manti':10000, 'somsa':12000,\
        'norin':14000, 'shorva':15000, 'shashlik':11000,\
        'chuchvara':18000, 'lag\'mon':18000, 'shovla':15000,\
        'mastava':10000, "moshxo'rda":14000}
ichimliklar = {'ayron':5000, 'sharbat':3000, "qora  choy":2000,\
               'ko\'k choy':2000}
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input('Iltimos, taom tanlang: ').lower())

ichimlikla=[]
for x in range(2):
    ichimlikla.append(input('Iltimos, ichimlik tanlang: ').lower())
for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom.title()} {menu[taom]} so'm")
    else:
        print(f"Kechirasiz, bizda {taom.title()} yo'q")
for ichim in ichimlikla:
    if ichim in ichimliklar:
        print(f"{ichim.title()} {ichimliklar[ichim]} so'm")
    else:
        print(f"Kechirasiz, bizda {ichim.title()} yo'q")      