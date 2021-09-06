# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:32:44 2021

@author: Oybek
"""

#N_7
#sonlarning bolinishini tekshirish

son = int(input("Butun son kiriting: "))
for n in range(2, 11):
    if not son%n:
        print(f"{son} {n} ga qoldiqsiz bo'linadi!")
