n=int(input())
a=list(map(int,input().split()))
k,m=map(int,input().split())
c=0
o=1
for i in a:
    if i>=k and i<=m:
        continue
    else:
        o=0
        print(i,end=" ")
if o==1:
    print(-1)