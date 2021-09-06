# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:31:48 2021

@author: Oybek
"""

#N_6
#login tekshirish

foydalanuvchilar = ['anvar', 'oybek', 'izzat', 'lochin']
login = input("Iltimos, login tanlang: ")
if login.lower() in foydalanuvchilar:
    print(f"{login} logini band, iltimos boshqa login tanlang!")
else:
    print(f"Xush kelibsiz, {login.title()}!")
