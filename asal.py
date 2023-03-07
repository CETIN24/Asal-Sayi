# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def asal(n):
   
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def asal_uret():
    
    for n in range(500, 600):
        if n % 2 == 0 or n % 5 == 0:
            continue
        if asal(n):
            print(n)

asal_uret()
