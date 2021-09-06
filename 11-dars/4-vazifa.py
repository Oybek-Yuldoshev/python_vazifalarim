# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:26:08 2021

@author: Oybek
"""

#N_4
#kichik korzinka:)

mahsulotlar = ['non', 'sariyog\'', 'choy', 'tuz', 'sabzi', 'guruch', 'moy', 'sut', 'shakar', 'tuxum', 'go\'sht']
savat =[]
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else: 
        print(f"Do'konimizda {mahsulot} yo'q")
