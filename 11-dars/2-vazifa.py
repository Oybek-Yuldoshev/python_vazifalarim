# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:21:57 2021

@author: Oybek
"""
#N_2
#bog' uchun chipta narxini hisoblash

yosh = int(input("Iltimos, yoshingizni kiriting: "))
if yosh < 4 or yosh > 60:
    print("Siz uchun kirish bepul")
elif yosh < 18:
    print("Kirish narxi 10000 so'm")
else:
    print("Kirish narxi 20000 so'm")
