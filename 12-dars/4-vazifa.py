# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:40:49 2021

@author: Oybek
"""

#N_4
#mahsulotlarni bor yoki yo'qligini tekshirish

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
    print("Savatingiz bo'sh")            