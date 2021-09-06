# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 16:01:04 2021

@author: Oybek
"""

#N_1
#Buyurtmalar qabul qilish

# print("Buyurtmalar qa'bul qilib olamiz!")
# buyurtmalar = []
# n=1
# while True:
#     savol = "Sizga qanday mahsulotlar kerak? \n"
#     buyurtma = input(savol)
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana buyurtma  berasizmi? \nha/yo'q\n")
#     if javob != "yo'q":
#         n+=1
#         continue
#     else:
#         break
# print("Buyurtmalar qa'bul qilinib olindi. \nBuyurtmalar ro'yhati:\n")
# n=1
# for  b in buyurtmalar:
#     print(f"{n}-{b}")
#     n+=1

#N_2
#e-bozor
# print("Mahsulotlar nomi va narxini kiritasiz! ")
# mahsulotlar = {}
# n = 1
# ishora = True 
# while ishora:
#     mahsulot = input(f"{n}-mahsulotni kiriting: ")
#     narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
#     mahsulotlar[mahsulot] = int(narx)
#     n+=1
#     javob = input("Yana mahsulot kiritasizmi? \nha/yo'q\n")
#     if javob == "yo'q":
#         ishora = False
# for x, y in mahsulotlar.items():        
#     print(f"{x.title()} ning narxi {y} so'm")
    
#N_3
#Mahsulotlar bor yoki yo'qligini tekshiramiz

# buyurtmalar = ['sut', 'un', 'non', "go'sht", 'moy']
# mahsulotlar = {'non': 1500, 'suv': 2000, 'sut': 5000}
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narx = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()}ning narxi - {narx} so'm")
#     else: print(f"Bizda {buyurtma} yo'q")
        