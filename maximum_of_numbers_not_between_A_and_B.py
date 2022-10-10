n=int(input())
a=list(map(int,input().split()))
k,m=map(int,input().split())
c=zz=-100000000
for i in a:
    if i>=k and i<=m:
        continue
    else:
        if i>c:
            c=i
if zz==c:
    print(-1)
else:
    print(c)