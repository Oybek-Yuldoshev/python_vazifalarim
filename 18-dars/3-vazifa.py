# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:00:58 2021

@author: Oybek
"""

#N_3
#Mahsulotlar bor yoki yo'qligini tekshiramiz

buyurtmalar = ['sut', 'un', 'non', "go'sht", 'moy']
mahsulotlar = {'non': 1500, 'suv': 2000, 'sut': 5000}
while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narx = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()}ning narxi - {narx} so'm")
    else: print(f"Bizda {buyurtma} yo'q")
      