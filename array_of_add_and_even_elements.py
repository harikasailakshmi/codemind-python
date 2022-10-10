n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
for i in a:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
print(*d,end=" ")
print(*c)