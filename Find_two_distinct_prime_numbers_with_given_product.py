def pm(a):
    for i in range(2,a):
        if a%i==0:
            return 0
    return 1
n=int(input())
a=0
b=0
for i in range(2,n+1):
    for j in range (2,n+1):
        if i*j==n:
            if pm(i)==1 and pm(j)==1:
                a=i
                b=j
if a!=0 and b!=0:
    print(b,a)
else:
    print("-1")
        