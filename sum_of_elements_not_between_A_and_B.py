n=int(input())
a=list(map(int,input().split()))
k,m=map(int,input().split())
c=0
for i in a:
    if i>=k and i<=m:
        continue
    else:
        c+=i
print(c)