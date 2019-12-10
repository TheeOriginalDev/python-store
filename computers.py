#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:47:24 2019

@author: devonjones
"""

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