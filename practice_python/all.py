# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:38:26 2025

@author: c.samanja09
"""

inv =["Sword", "Stick", "Numchuks"]

if all(inv):
    print('Inventory full!')    
elif any(inv):
    print('Inventory has items!')
else:
    print('Inventory empty!')