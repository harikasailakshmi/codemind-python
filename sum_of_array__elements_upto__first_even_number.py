n=int(input())
a=list(map(int,input().split()))
k=0
for i in a:
    if i%2==0:
        break
    else:
        k+=i
print(k)