# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:02:29 2021

@author: Oybek
"""
#N_3
#Do'stlarimning sevimli kinolari

kinolar = {
    'nodir':['Jumong', 'Tabib', 'Mening do\'stim jin'],
    'doston':['Snowden', 'Xavfli topshiriq', 'Uddalab bo\'lmas topshiriq'],
    'diyor':['Mortal Kombat', 'Yangi mutantlar', 'Qotil nishoni']
    }
for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)
