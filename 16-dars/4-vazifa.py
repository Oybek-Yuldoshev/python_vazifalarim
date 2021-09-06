# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:01:41 2021

@author: Oybek
"""
#N_4
#davlatlar haqida 

davlatlar ={
    'uzb':{
        'nom':'o\'zbekiston respublikasi',
        'poytaxt':'toshkent',
        'maydon':'447,8',
        'prezident':'shavkat mirziyoyev',
        'pul':'sum'
        },
    'rus':{
        'nom':'rossiya federatsiyasi',
        'poytaxt':'moskva',
        'maydon':'17130',
        'prezident':'vladimir putin',
        'pul':'rubl'
        },
    'usa':{
        'nom':"amerika qo\'shma shtatlari",
        'poytaxt':'washington',
        'maydon':'9834',
        'prezident':'joe bayden',
        'pul':'dollar'
        }
    }
for davlat, info in davlatlar.items():
    if davlat.lower()=='usa':
        davlat = davlat.upper()
    else:
        davlat.capitalize()
    print(f"\n{davlat} haqida ma'lumotlar:\n"
          f"To'liq nomi: {info['nom'].title()}\n"
          f"Potaxti: {info['poytaxt'].title()}\n"
          f"Maydoni: {info['maydon'].title()}\n"
          f"Prezidenti: {info['prezident'].title()}"
          f"Pul birligi: {info['pul'].title()}")

