import math
x,y=map(int,input().split())
temp=x
temp1=y
d=0
w=0
k=0
b=0
while(temp1):
    h=temp%10
    temp=temp//10
    temp1-=1
    k=k*10+h
while(k):
    t=k%10
    k=k//10
    b=b*10+t
while(x):
    n=x%10
    x=x//10
    d=d*10+n
while(y):
    z=d%10
    d=d//10
    y-=1
    w=w*10+z
a=abs(b-w)
print(a)