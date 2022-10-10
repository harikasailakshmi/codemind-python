def prime(a):
    if a<2:
        return 0
    else:
        for i in range(2,a):
            if a%i==0:
                return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if prime(i)==1:
        c+=1
print(c)