# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 17:38:31 2018

@author: Alassane-anand
"""

#%%
import random

trial_list = ['apple']

def word_selector(ls):
    word = random.choice(ls)
    word_star = word.replace(word, '*' * len(word))
    word_star = [i for i in word_star]
    return word, word_star
#%%
    
def guess_letter(score, word, word_star):
    life = 8
    while life > 0:
        print('Remaining trials : ', life)
        try:
            guess = str(input('Guess a letter : '))
        except:
            print('please enter a valid letter')
        if guess not in word:
            print('Wrong! Try again. Your current word to guess is', word_star)
            life -= 1
        else:
            for i in range(len(word)):
                if word[i] == guess:
                    word_star[i] = guess
            print('Correctomundo! this is your guess', word_star)
            life -= 1
            if '*' not in word_star:
                print('Good job! you won')
                score += life
                life = 0
                
    print('Your score is {0} '.format(score))            
    return score

#%%

def user():
    name = input('Enter your name : ')
    name = name + '.txt'
    with open(name, 'r') as file:
        file.seek(0)
        score = file.read(1)
        if not score:
            score = 0
        else:
            score = int(score)
        file.close()
    return score, name

def store_score(score, name) : 
    with open(name, 'w') as file:
        file.write(str(score))
        file.close()
        











       
            
            