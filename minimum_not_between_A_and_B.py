n=int(input())
a=list(map(int,input().split()))
k,m=map(int,input().split())
c=o=100000
for i in a:
    if i<k or i>m:
        if c>i:
            c=i
if c==o:
    print(-1)
else:
    print(c)