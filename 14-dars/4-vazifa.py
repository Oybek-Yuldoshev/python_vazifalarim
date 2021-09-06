# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 00:17:02 2021

@author: Oybek
"""
#N_4
#python izohli lug'ati 2
python = {'integer':'butun', 'float':'o\'nlik', 'if':'yoki', \
'print':'chop etmoq', 'title':'sarlavha', 'remove':'o\'chirmoq', \
'else':'yoki', 'in':'ichida', "for":'takrorlash', "upper":'kattalashtirish',\
'input':'kiritmoq', 'append':"qo'shmoq"}
kalit = input('Kalit so\'zni kiriting: ').lower()
tarjima = python.get(kalit)
if tarjima==None:
    print('Bunday so\'z mavjud emas')
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi!")
