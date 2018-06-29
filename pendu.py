# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 23:00:24 2018

@author: Alassane-anand
"""

from donnees import *
import fonctions
import os

while True:
    selection = input('Do you want to continue? Select Y or N : ')
    if selection == 'Y':
        score, file_name = user()
        word, word_star = word_selector(word_list)
        score = guess_letter(score, word, word_star)
    else:
        store_score(score, file_name)
        break
os.system('pause')

