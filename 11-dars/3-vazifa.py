# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:23:40 2021

@author: Oybek
"""

#N_3
#Sonlarni taqqoslovchi

son_1 = float(input("1-sonni kiriting: "))
son_2 = float(input("2-sonni kiriting: "))
if son_1 == son_2:
    print(f"{son_1}={son_2}")
elif son_1 > son_2:
    print(f"{son_1} katta {son_2} dan")
else:
    print(f"{son_1} kichik {son_2} dan")
