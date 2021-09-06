# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:39:26 2021

@author: Oybek
"""

#N_3
#katta va kichik sonlarni tekshirish

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")