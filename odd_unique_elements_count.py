n=int(input())
k=set(map(int,input().split()))
c=0
for i in k:
    if i%2!=0:
        c+=1
print(c)