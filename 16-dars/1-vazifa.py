# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:04:20 2021

@author: Oybek
"""
#N_1
#Adabiyot

navoiy ={
        'ism':'Alisher  Navoiy',
        'tyil':1441,
        'vyil':1501,
        'asarlar':'Xamsa, Mushokafat ul-qulub'}
bobur = {
    'ism':'Zahiriddin Muhammad Bobur',
    'tyil':1483,
    'vyil':1530,
    'asarlar':'Boburnoma, Hindiston'}
buxoriy = {
    'ism':'Abu Abdulloh Muhammad ibn Ismoil',
    'tyil':810,
    'vyil':870,
    'asarlar':'Sahih ul-Buxoriy'
           }
qodiriy = {
    'ism':'Abdulla Qodiriy',
    'tyil':1894,
    'vyil':1938,
    'asarlar':'O\'tgan kunlar, Mehrobdan chayon'       
           }

shaxslar = [navoiy, bobur, buxoriy, qodiriy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil = shaxs['tyil']
    vyil = shaxs['vyil']
    asarlar = shaxs['asarlar']
    print(f"{ism} {tyil}-yilda tavallud topgangan, {asarlar}ni yozgan.{vyil-tyil} umr ko'rgan. {vyil}-yilda vafot etgan")
