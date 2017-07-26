## 1.  Make Trinary Group (OOP)

### 1) Make Trinary Class
* object에 'a', 'b', 'c' 중 하나를 넣지 않으면, error 프린트하고 'a'를 넣어줌.
* ex) A = Trinary('k') → A : Trinary('a')
``` python
class Trinary(object):
    def __init__(self, elt):
        if(elt not in ['a','b','c']):
            self.e = 'a'
            print('Trinary must be in [a,b,c]')
            print("Set default 'a'")
        else:
            self.e = elt
```



### 2) Define Methods
* Add & multiple : 그냥 하나씩 정의

``` python
    def __add__(self, other):
        if self.e=='a':
            if other.e=='a':
                return Trinary('c')
            elif other.e=='b':
                return Trinary('c')
            else:
                return Trinary('b')
        elif self.e=='b':
            if other.e=='a':
                return Trinary('c')
            elif other.e=='b':
                return Trinary('a')
            else:
                return Trinary('a')
        else:
            if other.e=='a':
                return Trinary('b')
            elif other.e=='b':
                return Trinary('a')
            else:
                return Trinary('b')
    def __mul__(self,other):
        if self.e=='a':
            if other.e=='a':
                return Trinary('a')
            elif other.e=='b':
                return Trinary('a')
            else:
                return Trinary('a')
        elif self.e=='b':
            if other.e=='a':
                return Trinary('a')
            elif other.e=='b':
                return Trinary('b')
            else:
                return Trinary('c')
        else:
            if other.e=='a':
                return Trinary('a')
            elif other.e=='b':
                return Trinary('c')
            else:
                return Trinary('b')
```

* Power :
```python
    def __pow__(self, num):
        if num==1:
            return self
        else:
            return self*self**(num-1)
```
* String : self.e(string)과 '[Trinary]'(string)은 +를 이용하면 출력할 때 붙어서 나온다.

    ex) A가 Trinary('a')였다면, print(A) → a[Trinary]
```python
    def __str__(self):
        return self.e + '[Trinary]'
```

<br>

## 2. Orbit of the Earth (Numerical Integration)

* Use 'Runge Kutta method 4th order'
    * 수치 해석에서, 룽게-쿠타 방법은 미분 방정식 중 초기값 문제를 푸는 방법 중 하나이다.(by wiki)
    <img src="https://github.com/KayoungBan/CS/blob/master/Problem.3/rk1.PNG">
    
    * k1,k2,k3,k4를 구하는 방법은 아래와 같다.
    <img src="C:\Users\Bany\Documents\CS\Problem.3\rk5.png">

    * 여기서 ki들을 구하기 위해 F를 계산하면 다음과 같다.
    <img src="C:\Users\Bany\Documents\CS\Problem.3\rk2.png">

    * 이때 F=ma를 이용하여 a를 구해주면 다음과 같다.
    <img src="C:\Users\Bany\Documents\CS\Problem.3\rk3.png" width="70%" >    

    *  태양의 위치를 (0,0,0)으로 잡아주었으므로 dx=-x와 같다. 
    <img src="C:\Users\Bany\Documents\CS\Problem.3\rk4.png" width="70%">


* 이를 이용하여 a_i 들을 구하면,
```python
def a_x(x,y,z):
    
    return g_con*sun_m*(-x)/((x**2+y**2+z**2)**1.5)
```
* 위에서 구한 k1,k2,k3,k4를 구하면,
``` python
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
```
* x,y,z에 대한 좌표와 속력을 list로 입력

``` python
x_list = [x0,x1]

xv_list = [xv0]

for i in range(int(3650*24*3600/dt)):
    k1, k2, k3, k4, k1_v, k2_v, k3_v, k4_v = k_x(x_list[i],x_list[i+1],y_list[i+1],z_list[i+1], xv_list[i])

    x_list.append(x_list[i+1] + dt*(k1+2*k2+2*k3+k4)/6.0)
    xv_list.append(xv_list[i] + dt*(k1_v+2*k2_v+2*k3_v+k4_v)/6.0)    
```
* print and plot
``` python
print(x_list[-1]/AU,y_list[-1]/AU,z_list[-1]/AU)

plt.plot(x_list,label='x-axis')
plt.xlabel('time')  # x-axis
plt.ylabel('x(AU)')  # y-axis
plt.title('Dangerous')  # title
plt.show()  # plot show
```