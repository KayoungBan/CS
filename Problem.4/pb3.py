# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:47:15 2017

@author: Bany
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

g = pd.read_csv('data.csv')
x = g['x']
y = g['y']
z = g['z']
t = list(range(7301))


r = (x**2+y**2+z**2)**0.5
rr = []
root = []
root_t = []

for i in range(len(r)-1):
    rr.append(r[i+1]-r[i])


for i in range(len(rr)-1):  
    if (rr[i]*rr[i+1]<0):
        root.append(r[i+1])
        root_t.append(i+1)


fig = plt.figure(1)  
ax = fig.add_subplot(111, projection='3d')  
ax.plot(x, y, z)     


plt.figure(2)
plt.plot(t,r)
plt.plot(root_t,root,'ro')

plt.xlabel('time(half of a day)')  # x-axis
plt.xlabel('distance(AU)')  # y-axis
plt.title('Physics Test')  # title
plt.grid()  # grid
plt.legend()  # for label
plt.show()  # plot show

