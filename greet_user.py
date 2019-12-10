#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:45:20 2019

@author: devonjones
"""

#Function to greet the user and ask for a category

import pandas
pandas.set_option('display.max_columns', 1000 )
electronics = pandas.read_csv("electronics.csv")
tabletslist = list(electronics.Tablets)
computerslist = list(electronics.Computers)
laptopslist = list(electronics.Laptops)
def greet_user(greeting,sentinel,categoryq,readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    if canswer == "Tablets":
        tablets("Welcome to our Tablets section! Here are your choices:",tabletslist,"Which tablet would you like or enter None? ")
    elif canswer == "Computers":
        computers("Welcome to our Computers section!  Here are your choices:",computerslist,"Which computer would you like or enter None? ")
    elif canswer == "Laptops":
        laptops("Welcome to our Laptops section!  Here are your choices:",laptopslist,"Which laptop would you like or enter None? ")
    else:
        print('Sorry, we do not carry that category.  See you next time!')
