n=int(input())
k=list(input().split())
z=list(map(int,k))
a=len(str(min(z)))
c=0
for i in k:
    if a==len(i):
        c+=1
print(c)