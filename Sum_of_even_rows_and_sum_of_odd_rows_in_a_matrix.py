n,m=map(int,input().split())
k=[]
d=0
e=0
for i in range(n):
    a=list(map(int,input().split()))
    k.append(sum(a))
for i in range(n):
    if i%2==0:
        d+=k[i]
    else:
        e+=k[i]
print(d,e)