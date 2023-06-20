# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 18:59:12 2023

@author: kshit
"""
import random
import string

x = input("enter the word to be coded\n")
y = []
def secret():
    if len(x) >= 3:
        p = [*x]
        print(p)
        i = 0 
        j = 0 
        while i<3:
            p.append((random.choice(string.ascii_letters.lower())))
            i = i + 1
        print(p)
        while j<3:
            y.append((random.choice(string.ascii_letters.lower())))
            j = j + 1
        print(y)
        p.pop(0)
        print(p)
        q = y + p
        for char in q:
            print(char, end = '')
       


n = secret()
print(n)