# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:36:52 2021

@author: Oybek
"""

#N_2
#chipta narhini hisoblash

yosh = int(input("Yoshingiz nechida? \n"))
if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")
