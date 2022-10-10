n,m=map(int,input().split())
a=list(input().split())
c=0
for i in range(n):
    if len(str(abs(int(a[i]))))==m:
        c+=1
print(c)
