# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 21:16:30 2025

@author: c.samanja09
"""

def longer_than_4(string):
    return len(string)>4

strings=["my","world","apple","pear"]

filtered=filter(longer_than_4, strings)
print(list(filtered))