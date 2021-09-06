# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:38:33 2021

@author: Oybek
"""

#N_1
#yoqtirgan kitobigiz qaysi?

kitob = "Qaysi kitobni yoqtirasiz?"
kitob += " (dasturni to'xtatishlik uchun 'stop' so'zini kiriting)\n "
while True:
    qiymat = input(kitob)
    if qiymat == "stop":
        break
print("Rahmat!")
