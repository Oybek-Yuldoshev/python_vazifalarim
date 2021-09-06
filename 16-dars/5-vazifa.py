# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:00:38 2021

@author: Oybek
"""
#N_5
#davlatlar haqida malumot 2
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
davlat = input('Iltimos, biror davlatni tanglang:\n usa\n rus\n uzb\n').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    if davlat=='usa':
        davlat = davlat.upper()
    print(f"\n{davlat} haqida ma'lumotlar:\n"
          f"To'liq nomi: {info['nom'].title()}\n"
          f"Potaxti: {info['poytaxt'].title()}\n"
          f"Maydoni: {info['maydon'].title()}\n"
          f"Prezidenti: {info['prezident'].title()}\n"
          f"Pul birligi: {info['pul'].title()}")
        
