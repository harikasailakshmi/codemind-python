n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=k=-10000000
for i in a:
    if i>=x and i<=y:
        if s<i:
            s=i
if s==k:
    print("-1")
else:
    print(s)
