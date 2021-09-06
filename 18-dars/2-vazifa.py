# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:02:04 2021

@author: Oybek
"""

#N_2
#e-bozor

print("Mahsulotlar nomi va narxini kiritasiz! ")
mahsulotlar = {}
n = 1
ishora = True 
while ishora:
    mahsulot = input(f"{n}-mahsulotni kiriting: ")
    narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
    mahsulotlar[mahsulot] = int(narx)
    n+=1
    javob = input("Yana mahsulot kiritasizmi? \nha/yo'q\n")
    if javob == "yo'q":
        ishora = False
for x, y in mahsulotlar.items():        
    print(f"{x.title()} ning narxi {y} so'm")
    