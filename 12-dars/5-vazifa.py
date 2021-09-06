# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:49:34 2021

@author: Oybek
"""

# N_5
#korzinka

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
      print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")