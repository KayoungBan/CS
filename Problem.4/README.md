## 1.   Pi (Monte Carlo)

### 1) Make Trinary Class
* 필요한 변수
``` python
pi = math.pi

cnt1 = 0 # In 2D
cnt2 = 0 # In 3D

step = 0 # 공 던진 횟수
step2 = 0 # 공 던진 횟수 (In 3D)

pi1 = 0 # step회 던졌을 때 계산된 pi 값
pi2 = 0 # step회 던졌을 때 계산된 pi 값 (In 3D)

err1 = abs((pi-pi1)*100/pi) # 계산된 pi 값과 실제 pi값 에러
err2 = abs((pi-pi2)*100/pi) # 계산된 pi 값과 실제 pi값 에러
```
* 원하는 Error 임계
``` python
threshold = float(input("Please threshold (%) = ")) 
```
* 2D
``` python
while(err1>threshold): # 에러가 설정된 에러율보다 크다면 공 또 던짐

    x = rd.random()*2-1 # 랜덤발생
    y = rd.random()*2-1

    if (x**2+y**2<=1): # 원안에 공이 박혔는지 확인
        cnt1+=1 # 박혔다면 횟수 증가

    step+=1 #공 던진횟수 증가
    pi1 = cnt1/step*4 # 한회 시행했을때 수정된 pi 값 계산
    err1 = abs((pi-pi1)*100/pi) # 수정된 에러 계산
```
* 2D
``` python
while(err2>threshold): # 에러가 설정된 에러율보다 크다면 공 또 던짐
    x = rd.random()*2-1 # 랜덤발생
    y = rd.random()*2-1
    z = rd.random()*2-1 

    if (x**2+y**2+z**2<=1): # 원안에 공이 박혔는지 확인
        cnt2+=1 #박혔다면 횟수 증가

    step2+=1 #공 던진횟수 증가
    pi2 = cnt2/step2*6 # 한회 시행했을때 수정된 pi 값 계산
    err2 = abs((pi-pi2)*100/pi) #수정된 에러 계산
```

### 2) Numerical Root Finding
* 범위 ([a,b]), N 값을 정해줌

``` python
    a=float(input("Left Interval: "))
    b=float(input("Right Interval: "))
    N=int(input("How many iterations? "))
```

* 함수 설정 for polynomial, sin, cos function
```python
import math as mt

def F(x):

    f = x - mt.cos(x)

    return f
```
* 함수 설정 for Ai(x)
```python
import scipy.special as sc

def F(x):

    f = sc.airy(x)

    return f[0]
```
* 필요한 list
    * x+dx list 'l' 설정
    * F(x+dx) list 'f1' 설정
    * x축을 지나는 x 값의 index i를 갖는 list 'f2' 설정
```python
l = [a+(b-a)*k/N for k in range(N)]
fl = [F(l[i]) for i in range(N)]

f2 = [i for i in range(N-1) if fl[i]*fl[i+1]<=0]
```
* 가끔 발생하는 Error에 대한 대책
ex) root = [1.9999999,2]
```python
for i in range(len(f2)-1):
    if (abs(f2[i+1]-f2[i])==1):
        l[f2[i]]=l[f2[i+1]]
        f2.remove(f2[i+1])
```
* Root를 갖는 list 'root'와 print
```python
root = [l[f2[i]] for i in range(len(f2))]
print("Root is", root)
```


## 3. Find Local Maxima of Numerical function

* data 불러오기 및 만들기
```python
import pandas as pd
import matplotlib.pyplot as plt

g = pd.read_csv('data.csv')
x = g['x']
y = g['y']
z = g['z']
t = list(range(7301))

r = (x**2+y**2+z**2)**0.5
```
* 이를 이용하여 a_i 들을 구하면,
```python
rr = []
root = []
root_t = []
```
* 위에서 구한 k1,k2,k3,k4를 구하면,
``` python
for i in range(len(r)-1):
    rr.append(r[i+1]-r[i])


for i in range(len(rr)-1):  
    if (rr[i]*rr[i+1]<0):
        root.append(r[i+1])
        root_t.append(i+1)
```
* x,y,z에 대한 좌표와 속력을 list로 입력

``` python

```
* print and plot
``` python

```