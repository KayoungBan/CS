# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:10:15 2017

@author: Bany
"""

import datetime 
import random as rd
import math


pi = math.pi
cnt1 = 0 # In 2D
cnt2 = 0 # In 3D
step = 0 # 공 던진 횟수
step2 = 0 # 공 던진 횟수 (In 3D)
pi1 = 0 # step회 던졌을 때 계산된 pi 값
pi2 = 0 # step회 던졌을 때 계산된 pi 값 (In 3D)
err1 = abs((pi-pi1)*100/pi) # 계산된 pi 값과 실제 pi값 에러
err2 = abs((pi-pi2)*100/pi) # 계산된 pi 값과 실제 pi값 에러

threshold = float(input("Please threshold (%) = ")) # 임계 error%

start1 = datetime.datetime.now()  # check start time 
while(err1>threshold): # 에러가 설정된 에러율보다 크다면 공 또 던짐
    x = rd.random()*2-1 # 랜덤발생
    y = rd.random()*2-1 #''
    if (x**2+y**2<=1): # 원안에 공이 박혔는지 확인
        cnt1+=1 # 박혔다면 횟수 증가
    step+=1 #공 던진횟수 증가
    pi1 = cnt1/step*4 # 한회 시행했을때 수정된 pi 값 계산
    err1 = abs((pi-pi1)*100/pi) # 수정된 에러 계산

end1 = datetime.datetime.now()  # check end time
    
print("Running time : " , end1-start1)  # calculate running time
print("Number of times ball was thrown : ", step)
print("In 2D, pi is " , pi1)
print("We know pi is ", pi)
print("Error is " , err1, "\n")



start2 = datetime.datetime.now()  # check start time 
while(err2>threshold): # 에러가 설정된 에러율보다 크다면 공 또 던짐
    x = rd.random()*2-1 #랜덤발생
    y = rd.random()*2-1 #''
    z = rd.random()*2-1 #''
    if (x**2+y**2+z**2<=1): # 원안에 공이 박혔는지 확인
        cnt2+=1 #박혔다면 횟수 증가
    step2+=1 #공 던진횟수 증가
    pi2 = cnt2/step2*6 # 한회 시행했을때 수정된 pi 값 계산
    err2 = abs((pi-pi2)*100/pi) #수정된 에러 계산

end2 = datetime.datetime.now()  # check end time
    
print("Running time : " , end2-start2)  # calculate running time
print("Number of times ball was thrown : ", step2)
print("In 3D, pi is " , pi2)
print("We know pi is ", pi)
print("Error is " , err2, "\n")



