# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:02:40 2021

@author: Oybek
"""
#N_1
#Buyurtmalar qa'bul qilib olish
print("Buyurtmalar qa'bul qilib olamiz!")
buyurtmalar = []
n=1
while True:
    savol = "Sizga qanday mahsulotlar kerak? \n"
    buyurtma = input(savol)
    buyurtmalar.append(buyurtma)
    javob = input("Yana buyurtma  berasizmi? \nha/yo'q\n")
    if javob != "yo'q":
        n+=1
        continue
    else:
        break
print("Buyurtmalar qa'bul qilinib olindi. \nBuyurtmalar ro'yhati:\n")
n=1
for  b in buyurtmalar:
    print(f"{n}-{b}")
    n+=1
