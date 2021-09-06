# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 00:16:06 2021

@author: Oybek
"""
#N_3
#python izohli lug'ati
python = {'integer':'butun', 'float':'o\'nlik', 'if':'yoki', \
'print':'chop etmoq', 'title':'sarlavha', 'remove':'o\'chirmoq', \
'else':'yoki', 'in':'ichida', "for":'takrorlash', "upper":'kattalashtirish',\
'input':'kiritmoq', 'append':"qo'shmoq"}
kalit = input('Kalit so\'zni kiriting: ').lower()
print(python.get(kalit, 'Bunday so\'z mavjud emas'))
