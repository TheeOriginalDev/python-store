#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:46:33 2019

@author: devonjones
"""

#Function ask user to pick Tablet
def tablets(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    tabletpick = input(pickq)
    if tabletpick == "None":
        print("Goodbye")
    elif tabletpick == "iPad Pro":
        closing("iPad Pro",25,"Enjoy your iPad Pro!")
    elif tabletpick == "iPad Air":
        closing("iPad Air",50,"Enjoy your iPad Air!")
    elif tabletpick == "iPad Mini":
        closing("iPad Mini",75,"Enjoy your iPad Mini!")
    elif tabletpick == "Galaxy Tablet":
        closing("Galaxy Tablet",20,"Enjoy your Galaxy Tablet!")
    else:
        closing("Amazon Fire",100,"Enjoy your Amazon Fire!")