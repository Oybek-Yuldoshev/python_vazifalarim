# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:59:56 2021

@author: Oybek
"""


#N_1
#yoqtirgan kitobigiz qaysi?

# kitob = "Qaysi kitobni yoqtirasiz?"
# kitob += " (dasturni to'xtatishlik uchun 'stop' so'zini kiriting)\n "
# while True:
#     qiymat = input(kitob)
#     if qiymat == "stop":
#         break
# print("Rahmat!")

# #N_2
# #chipta narxi qancha?
# savol = "Yoshingizni kiriting: "
# savol += "(dasturni to'xtatishlik uchun 'exit' yoki 'quit' deb yozing) \n"

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     x = f"Chipta  narxi {yosh} yoshlilar uchun "
#     if yosh < 7:
#         narx = 2000
#     elif 7 <= yosh < 18:
#         narx = 3000
#     elif 18 <= yosh < 65:
#         narx = 10000
#     else:
#         narx=0
#     if narx == 0:
#         print(f"{x} bepul")
#     else:
#         print(f"{x} {narx} so'm")

# print("TASHAKKUR")

# #N_3
# #Kiritilgan sonning ildizini qaytaruvchi dastur.

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = float(input(savol))
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")