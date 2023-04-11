#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:35:54 2023

@author: wangbinb
"""

import numpy as np
import matplotlib.pyplot as plt
import time



Np = 1000 # number of particles 
dt = 0.1
dx = 0.1
tend = 1
t = np.arange(0,tend,dt)

# define the initial particle locatioin, x0 = 0 for every particle 
x0 = np.zeros(Np) 



# ######################################
# ### 1: a step-by-step demo
# ######################################
# # Initialize iteration
# x = x0
# for ti in t:    
#     plt.figure(1)
#     plt.clf()
#     # create a list of random number with uniform distribution in the range of (-1,1)
#     random_number = np.random.uniform(low=-1, high=1, size=Np)
#     step = dx * (random_number >= 0) + (-dx) * (random_number < 0)
#     x = x+step
#     plt.plot(x,'.')
#     plt.show()
#     input("Press Enter to continue...")
# ######################################    
    
 
# ########################################################
# ### 2: Let's run this code for a longer time
# ########################################################
x = x0
tend = 100
t = np.arange(0,tend,dt) 
for ti in t:    
    # create a list of random number with uniform distribution in the range of (-1,1)
    random_number = np.random.uniform(low=-1, high=1, size=Np)
    step = dx * (random_number >= 0) + (-dx) * (random_number < 0)
    x = x+step

plt.hist(x)
plt.title('Random-walk after ' + str(int(tend/dt)) + ' steps' )



# ########################################################
# ### 3: Check the concentration 
# ########################################################
hist, bin_edges = np.histogram(x, density=True)
bin_center = 0.5 * (bin_edges[:-1] + bin_edges[1:])
delt_x = np.diff(bin_edges)
D = dx**2/(2*dt)
c = 1/np.sqrt(4*np.pi*D*tend) * np.exp(-bin_edges**2/(4*D*tend))

plt.figure()
plt.plot(bin_center, hist)
plt.plot(bin_edges, c)











