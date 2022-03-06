# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:39:40 2021

@author: Clau
"""

from core import User, np
User_list = []

#Definig users

Public_lighting = User("Public lighting ", 30)
User_list.append(Public_lighting)

#Appliances

Public_lighting_lamp_post = Public_lighting.Appliance(Public_lighting,12,40,2,310,0,300, 'yes', flat = 'yes')
Public_lighting_lamp_post.windows([0,362],[1082,1440],0.1)