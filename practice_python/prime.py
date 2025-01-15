# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:33:12 2025

@author: c.samanja09
"""

nums=range(1,10000)

def is_prime(num):
    for x in range(2,num):
        if(num%x) == 0:
            return False
    return True

primes=list(filter(is_prime,nums))

print(primes)