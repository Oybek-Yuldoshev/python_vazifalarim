# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:03:25 2021

@author: Oybek
"""
#N_2
#Adabiyot 2

navoiy ={
        'ism':'Alisher  Navoiy',
        'tyil':1441,
        'vyil':1501,
        'asarlar':'Xamsa, Mushokafat ul-qulub',
        'tjoy':'Hirot'}
bobur = {
    'ism':'Zahiriddin Muhammad Bobur',
    'tyil':1483,
    'vyil':1530,
    'asarlar':'Boburnoma, Hindiston',
    'tjoy':'Andijon'}
buxoriy = {
    'ism':'Abu Abdulloh Muhammad ibn Ismoil',
    'tyil':810,
    'vyil':870,
    'asarlar':'Sahih ul-Buxoriy',
    'tjoy':'Buxoro'}
qodiriy = {
    'ism':'Abdulla Qodiriy',
    'tyil':1894,
    'vyil':1938,
    'asarlar':'O\'tgan kunlar, Mehrobdan chayon',       
    'tjoy':'Toshkent'}

shaxslar = [navoiy, bobur, buxoriy, qodiriy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil = shaxs['tyil']
    vyil = shaxs['vyil']
    asarlar = shaxs['asarlar']
    tjoy = shaxs['tjoy']
    print(f"{ism} {tyil}-yili {tjoy}da tavallud topgangan, {asarlar} asarlarini yozgan.{vyil-tyil} umr ko'rgan. {vyil}-yilda vafot etgan")

