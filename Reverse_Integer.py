x=int(input())
k=0
temp=abs(x)
if x>0:
    while x:
        d=x%10
        x=x//10
        k=k*10+d
    print(k)
else:
    while temp:
        d=temp%10
        temp=temp//10
        k=k*10+d
    print(-k)