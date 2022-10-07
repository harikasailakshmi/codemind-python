def prime(a):
    if a<2:
        return 0
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return 0
        return 1
a=int(input())
a=a+1
c=0
while str(a)!=(str(a)[::-1]) or prime(a)!=1:
        a+=1
print(a)

    