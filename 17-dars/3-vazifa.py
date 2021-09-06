# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:36:20 2021

@author: Oybek
"""

#N_3
#Kiritilgan sonning ildizini qaytaruvchi dastur.

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")