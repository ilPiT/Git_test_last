# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:10:37 2022

@author: pietr,Clau
"""
'''
Paper: Energy sufficiency, lowlands.
User: Low Income Household
'''

#### Only house hold with poverty: 96%

from core import User, np
User_list = []

#Defining users -- LI
H1 = User("low income", 62) 
User_list.append(H1)
    
#Appliances
H1_indoor_bulb = H1.Appliance(H1,3,7,2,120,0.2,10)
H1_indoor_bulb.windows([1082,1440],[0,30],0.35)

H1_outdoor_bulb = H1.Appliance(H1,1,13,2,600,0.2,10)
H1_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H1_TV = H1.Appliance(H1,1,60,3,90,0.1,5)
H1_TV.windows([750,840],[1082,1440],0.35,[0,30])

H1_Antenna = H1.Appliance(H1,1,8,3,90,0.1,5)
H1_Antenna.windows([750,840],[1082,1440],0.35,[0,30])

H1_Phone_charger = H1.Appliance(H1,2,2,1,300,0.2,5)
H1_Phone_charger.windows([1080,1440],[0,0],0.35)


#Defining users -- HI
H2 = User("high income", 3)
User_list.append(H2)

#Appliances
H2_indoor_bulb = H2.Appliance(H2,4,7,2,120,0.2,10)
H2_indoor_bulb.windows([1082,1440],[0,30],0.35)
         
H2_outdoor_bulb = H2.Appliance(H2,2,13,2,600,0.2,10)
H2_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H2_TV = H2.Appliance(H2,2,60,2,120,0.1,5)
H2_TV.windows([1082,1440],[0,60],0.35)

H2_DVD = H2.Appliance(H2,1,8,2,40,0.1,5)
H2_DVD.windows([1082,1440],[0,60],0.35)

H2_Antenna = H2.Appliance(H2,1,8,2,80,0.1,5)
H2_Antenna.windows([1082,1440],[0,60],0.35)

H2_Radio = H2.Appliance(H2,1,36,2,60,0.1,5)
H2_Radio.windows([390,450],[1082,1260],0.35)

H2_Phone_charger = H2.Appliance(H2,4,2,2,300,0.2,5)
H2_Phone_charger.windows([1110,1440],[0,30],0.35)

H2_Freezer = H2.Appliance(H2,1,200,1,1440,0,30, 'yes',2)
H2_Freezer.windows([0,1440],[0,0])
H2_Freezer.specific_cycle_1(5,15,200,15)
H2_Freezer.specific_cycle_2(200,10,5,20)
H2_Freezer.cycle_behaviour([480,1200],[0,0],[0,479],[1201,1440])

H2_Mixer = H2.Appliance(H2,1,50,3,30,0.1,1, occasional_use = 0.33)
H2_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

H2_Fan = H2.Appliance(H2,1,171,1,220,0.27,60)
H2_Fan.windows([720,1080],[0,0])

H2_Laptop = H2.Appliance(H2,1,70,1,90,0.3,30)
H2_Laptop.windows([960,1200],[0,0])