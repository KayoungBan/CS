# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:08:47 2017

@author: Bany
"""

import matplotlib.pyplot as plt  # need to plot


g_con = 6.67259e-11
sun_m = 1.9891e30
AU = 1.49597870691e11

x0 = -9.851920196143998e-1*AU
y0 = 1.316466809434336e-1*AU
z0 = -4.877392224782687e-6*AU

x1 = -9.864337701483683e-1*AU
y1 = 1.230799243164879e-1*AU
z1 = -4.374019384763304e-6*AU

dt = 43200.0
xv0 = (x1-x0)/dt
yv0 = (y1-y0)/dt
zv0 = (z1-z0)/dt

def a_x(x,y,z):
    
    return g_con*sun_m*(-x)/((x**2+y**2+z**2)**1.5)

def a_y(x,y,z):
    
    return g_con*sun_m*(-y)/((x**2+y**2+z**2)**1.5)

def a_z(x,y,z):
    
    return g_con*sun_m*(-z)/((x**2+y**2+z**2)**1.5)


def k_x(x0,x1,y1,z1,v):
    
    k1 = (x1-x0)/dt
    k1_v = a_x(x1,y1,z1)
    
    k2 = v + dt*a_x(x1,y1,z1)/2.0
    k2_v = a_x(x1+dt*k1/2.0,y1+dt*k1/2.0,z1+dt*k1/2.0)
    
    k3 = v + dt*a_x(x1+dt*k1/2.0,y1+dt*k1/2.0,z1+dt*k1/2.0)/2.0
    k3_v = a_x(x1+dt*k2/2.0,y1+dt*k2/2.0,z1+dt*k2/2.0)
    
    k4 = v + dt*a_x(x1+dt*k2/2.0,y1+dt*k2/2.0,z1+dt*k2/2.0)
    k4_v = a_x(x1+dt*k3,y1+dt*k3,z1+dt*k3)
    
    return(k1,k2,k3,k4,k1_v,k2_v,k3_v,k4_v)

def k_y(y0,x1,y1,z1,v):
    
    k1 = (y1-y0)/dt
    k1_v = a_y(x1,y1,z1)
    
    k2 = v + dt*a_y(x1,y1,z1)/2.0
    k2_v = a_y(x1+dt*k1/2.0,y1+dt*k1/2.0,z1+dt*k1/2.0)   
    
    k3 = v + dt*a_y(x1+dt*k1/2.0,y1+dt*k1/2.0,z1+dt*k1/2.0)/2.0
    k3_v = a_y(x1+dt*k2/2.0,y1+dt*k2/2.0,z1+dt*k2/2.0) 
     
    k4 = v + dt*a_y(x1+dt*k2/2.0,y1+dt*k2/2.0,z1+dt*k2/2.0)
    k4_v = a_y(x1+dt*k3,y1+dt*k3,z1+dt*k3)    

    return(k1,k2,k3,k4,k1_v,k2_v,k3_v,k4_v)

def k_z(z0,x1,y1,z1,v):
    
    k1 = (z1-z0)/dt
    k1_v = a_z(x1,y1,z1)    
    
    k2 = v + dt*a_z(x1,y1,z1)/2.0
    k2_v = a_z(x1+dt*k1/2.0,y1+dt*k1/2.0,z1+dt*k1/2.0)    
    
    k3 = v + dt*a_z(x1+dt*k1/2.0,y1+dt*k1/2.0,z1+dt*k1/2.0)/2.0
    k3_v = a_z(x1+dt*k2/2.0,y1+dt*k2/2.0,z1+dt*k2/2.0)    
     
    k4 = v + dt*a_z(x1+dt*k2/2.0,y1+dt*k2/2.0,z1+dt*k2/2.0)
    k4_v = a_z(x1+dt*k3,y1+dt*k3,z1+dt*k3)    

    return(k1,k2,k3,k4,k1_v,k2_v,k3_v,k4_v)

x_list = [x0,x1]
y_list = [y0,y1]
z_list = [z0,z1]

xv_list = [xv0]
yv_list = [yv0]
zv_list = [zv0]


for i in range(int(3650*24*3600/dt)):
    k1, k2, k3, k4, k1_v, k2_v, k3_v, k4_v = k_x(x_list[i],x_list[i+1],y_list[i+1],z_list[i+1], xv_list[i])

    x_list.append(x_list[i+1] + dt*(k1+2*k2+2*k3+k4)/6.0)
    xv_list.append(xv_list[i] + dt*(k1_v+2*k2_v+2*k3_v+k4_v)/6.0)    
    
    k1, k2, k3, k4, k1_v, k2_v, k3_v, k4_v = k_y(y_list[i],x_list[i+1],y_list[i+1],z_list[i+1], yv_list[i])

    y_list.append(y_list[i+1] + dt*(k1+2*k2+2*k3+k4)/6.0)  
    yv_list.append(yv_list[i] + dt*(k1_v+2*k2_v+2*k3_v+k4_v)/6.0)      
    
    k1, k2, k3, k4, k1_v, k2_v, k3_v, k4_v = k_z(z_list[i],x_list[i+1],y_list[i+1],z_list[i+1], zv_list[i])

    z_list.append(z_list[i+1] + dt*(k1+2*k2+2*k3+k4)/6.0)
    zv_list.append(zv_list[i] + dt*(k1_v+2*k2_v+2*k3_v+k4_v)/6.0)      


print(x_list[-1]/AU,y_list[-1]/AU,z_list[-1]/AU)

plt.plot(x_list,label='x-axis')
plt.plot(y_list,label='y-axis')
plt.plot(z_list,label='z-axis')
plt.xlabel('time')  # x-axis
plt.ylabel('x/y/z')  # y-axis
plt.title('Dangerous')  # title
plt.show()  # plot show












