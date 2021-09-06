# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 12:29:21 2021

@author: Oybek
"""
# #N_1
# #Adabiyot

# navoiy ={
#         'ism':'Alisher  Navoiy',
#         'tyil':1441,
#         'vyil':1501,
#         'asarlar':'Xamsa, Mushokafat ul-qulub'}
# bobur = {
#     'ism':'Zahiriddin Muhammad Bobur',
#     'tyil':1483,
#     'vyil':1530,
#     'asarlar':'Boburnoma, Hindiston'}
# buxoriy = {
#     'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#     'tyil':810,
#     'vyil':870,
#     'asarlar':'Sahih ul-Buxoriy'
#            }
# qodiriy = {
#     'ism':'Abdulla Qodiriy',
#     'tyil':1894,
#     'vyil':1938,
#     'asarlar':'O\'tgan kunlar, Mehrobdan chayon'       
#            }

# shaxslar = [navoiy, bobur, buxoriy, qodiriy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     asarlar = shaxs['asarlar']
#     print(f"{ism} {tyil}-yilda tavallud topgangan, {asarlar}ni yozgan.{vyil-tyil} umr ko'rgan. {vyil}-yilda vafot etgan")
    
    
# #N_2
# #Adabiyot 2

# navoiy ={
#         'ism':'Alisher  Navoiy',
#         'tyil':1441,
#         'vyil':1501,
#         'asarlar':'Xamsa, Mushokafat ul-qulub',
#         'tjoy':'Hirot'}
# bobur = {
#     'ism':'Zahiriddin Muhammad Bobur',
#     'tyil':1483,
#     'vyil':1530,
#     'asarlar':'Boburnoma, Hindiston',
#     'tjoy':'Andijon'}
# buxoriy = {
#     'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#     'tyil':810,
#     'vyil':870,
#     'asarlar':'Sahih ul-Buxoriy',
#     'tjoy':'Buxoro'}
# qodiriy = {
#     'ism':'Abdulla Qodiriy',
#     'tyil':1894,
#     'vyil':1938,
#     'asarlar':'O\'tgan kunlar, Mehrobdan chayon',       
#     'tjoy':'Toshkent'}

# shaxslar = [navoiy, bobur, buxoriy, qodiriy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     asarlar = shaxs['asarlar']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yili {tjoy}da tavallud topgangan, {asarlar} asarlarini yozgan.{vyil-tyil} umr ko'rgan. {vyil}-yilda vafot etgan")


# #N_3
# #Do'stlarimning sevimli kinolari

# kinolar = {
#     'nodir':['Jumong', 'Tabib', 'Mening do\'stim jin'],
#     'doston':['Snowden', 'Xavfli topshiriq', 'Uddalab bo\'lmas topshiriq'],
#     'diyor':['Mortal Kombat', 'Yangi mutantlar', 'Qotil nishoni']
#     }
# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)
    
# #N_4
# #davlatlar haqida 

# davlatlar ={
#     'uzb':{
#         'nom':'o\'zbekiston respublikasi',
#         'poytaxt':'toshkent',
#         'maydon':'447,8',
#         'prezident':'shavkat mirziyoyev',
#         'pul':'sum'
#         },
#     'rus':{
#         'nom':'rossiya federatsiyasi',
#         'poytaxt':'moskva',
#         'maydon':'17130',
#         'prezident':'vladimir putin',
#         'pul':'rubl'
#         },
#     'usa':{
#         'nom':"amerika qo\'shma shtatlari",
#         'poytaxt':'washington',
#         'maydon':'9834',
#         'prezident':'joe bayden',
#         'pul':'dollar'
#         }
#     }
# for davlat, info in davlatlar.items():
#     if davlat.lower()=='usa':
#         davlat = davlat.upper()
#     else:
#         davlat.capitalize()
#     print(f"\n{davlat} haqida ma'lumotlar:\n"
#           f"To'liq nomi: {info['nom'].title()}\n"
#           f"Potaxti: {info['poytaxt'].title()}\n"
#           f"Maydoni: {info['maydon'].title()}\n"
#           f"Prezidenti: {info['prezident'].title()}"
#           f"Pul birligi: {info['pul'].title()}")

# #N_5
# #davlatlar haqida malumot 2
# davlatlar ={
#     'uzb':{
#         'nom':'o\'zbekiston respublikasi',
#         'poytaxt':'toshkent',
#         'maydon':'447,8',
#         'prezident':'shavkat mirziyoyev',
#         'pul':'sum'
#         },
#     'rus':{
#         'nom':'rossiya federatsiyasi',
#         'poytaxt':'moskva',
#         'maydon':'17130',
#         'prezident':'vladimir putin',
#         'pul':'rubl'
#         },
#     'usa':{
#         'nom':"amerika qo\'shma shtatlari",
#         'poytaxt':'washington',
#         'maydon':'9834',
#         'prezident':'joe bayden',
#         'pul':'dollar'
#         }
#     }
# davlat = input('Iltimos, biror davlatni tanglang:\n usa\n rus\n uzb\n').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     if davlat=='usa':
#         davlat = davlat.upper()
#     print(f"\n{davlat} haqida ma'lumotlar:\n"
#           f"To'liq nomi: {info['nom'].title()}\n"
#           f"Potaxti: {info['poytaxt'].title()}\n"
#           f"Maydoni: {info['maydon'].title()}\n"
#           f"Prezidenti: {info['prezident'].title()}\n"
#           f"Pul birligi: {info['pul'].title()}")
        