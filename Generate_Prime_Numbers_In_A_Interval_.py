def prime(a):
    c=0
    if a==1:
        c=1
    else:
        for i in range(2,a):
            if(a%i)==0:
                c=1
                break
    if c==0:
        return 0
    else:
        return 1
n=int(input())
m=int(input())
c=1
for i in range(n,m+1):
    if prime(i)==0:
        print(i)
    