#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:32:25 2019

@author: devonjones
"""

#Team Project -- Shopping Application

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
    

#Function ask user to pick a Computer
def computers(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    computerpick = input(pickq)
    if computerpick == "None":
        print("Goodbye")
    elif computerpick == "CyberPowerPC i7":
        closing("CyberPowerPC i7",155,"Enjoy your CyberPowerPC i7!")
    elif computerpick == "Pavilion Desktop i7":
        closing("Pavilion Desktop i7",75,"Enjoy your Pavilion Desktop i7!")
    elif computerpick == "OMEN Obelisk i7":
        closing("OMEN Obelisk i7",125,"Enjoy your OMEN Obelisk i7!")
    elif computerpick == "iBUYPOWER i5":
        closing("iBUYPOWER i5",135,"Enjoy your iBUYPOWER i5!")
    else:
        closing("OptiPlex i5",150,"Enjoy your OptiPlex i5!")
        
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
        
#Function to give user total price of purchase
def closing(pickeditem,price,goodbye):
    print("Your cost for the",pickeditem,"is $"+str(price))
    more = input("Would you like to pick another item (y/n)?")
    if more == "y":
        greet_user("Great!", "n", "What category would you like to browse (Tablets, Computers, Laptops)? ", "Ready to browse (y/n)? ")
    else:
        for l in goodbye:
            print(l)
    
    
        
greet_user("Welcome to our store", "n", "What category would you like to browse (Tablets, Computers, Laptops)? ", "Ready to browse (y/n)? ")
