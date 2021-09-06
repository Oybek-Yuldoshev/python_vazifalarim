# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:37:05 2021

@author: Oybek
"""

#N_2
#chipta narxi qancha?

savol = "Yoshingizni kiriting: "
savol += "(dasturni to'xtatishlik uchun 'exit' yoki 'quit' deb yozing) \n"

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    x = f"Chipta  narxi {yosh} yoshlilar uchun "
    if yosh < 7:
        narx = 2000
    elif 7 <= yosh < 18:
        narx = 3000
    elif 18 <= yosh < 65:
        narx = 10000
    else:
        narx=0
    if narx == 0:
        print(f"{x} bepul")
    else:
        print(f"{x} {narx} so'm")

print("TASHAKKUR")