def prime(a):
    c=0
    for i in range(2,int(a**0.5)+1):
        if (a%i==0):
            c+=1
            break
    if (c==0):
        return 1
    else:
        return 0
a=int(input())
b=int(input())
d=0
if(a<=1):
    a=2
for i in range(a,b+1):
    if(prime(i)==1):
        d+=1
print(d)