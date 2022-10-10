n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=[]
k=[]
for i in a:
    if i>=x and i<=y:
        s.append(i)
if s==k:
    print("-1")
else:
    print(*s)
