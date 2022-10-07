def prime(a):
    if a<2:
        return 0
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return 0
        return 1
a=int(input())
b=int(input())
c=a+b+1
k=a+b
while prime(c)!=1:
        c+=1
print(c-k)
    