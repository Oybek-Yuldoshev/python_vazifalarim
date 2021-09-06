# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:27:53 2021

@author: Oybek
"""

#N_5
#korzinkacha

mahsulotlar = ['non', 'sariyog\'', 'choy', 'tuz', 'sabzi', 'guruch', 'moy', 'sut', 'shakar', 'tuxum', 'go\'sht']
soralganlari = []
bor_mahsulotlar = []
mavjud_emas = []

for n in range(5):
    soralganlari.append(input("Qaysi mahsulotlar kerak? "))
for mahsulot in soralganlari:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas == []:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor!")
else:
    print(f"Quyidagi mahsulotlar do'konimizda yo'q: {mavjud_emas}")
