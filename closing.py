#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:50:05 2019

@author: devonjones
"""

#Function to give user total price of purchase
def closing(pickeditem,price,goodbye):
    print("Your cost for the",pickeditem,"is $"+str(price))
    more = input("Would you like to pick another item (y/n)?")
    if more == "y":
        greet_user("Great!", "n", "What category would you like to browse (Tablets, Computers, Laptops)? ", "Ready to browse (y/n)? ")
    else:
        for l in goodbye:
            print(l)