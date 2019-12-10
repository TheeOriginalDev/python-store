#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:48:08 2019

@author: devonjones
"""

#Function ask user to pick a Laptop
def laptops(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    laptoppick = input(pickq)
    if laptoppick == "None":
        print("Goodbye")
    elif laptoppick == "Pixelbook 13.3":
        closing("Pixelbook 13.3",1500,"Enjoy your Pixelbook 13.3!")
    elif laptoppick == "Samsung Chromebook 11.6":
        closing("Samsung Chromebook 11.6",750,"Enjoy your Samsung Chromebook 11.6!")
    elif laptoppick == "Lenovo 2in1 11.6":
        closing("Lenovo 2in1 11.6",800,"Enjoy your Lenovo 2in1 11.6!")
    elif laptoppick == "Dell Inspiron 15.6":
        closing("Dell Inspiron 15.6",900,"Enjoy your Dell Inspiron 15.6!")
    else:
        closing("MacBook",1000,"Enjoy your MacBook")