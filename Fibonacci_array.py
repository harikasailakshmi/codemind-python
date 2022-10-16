n=int(input())
a=list(map(int,input().split()))
x=a[0]
y=a[1]
c=0
flag=0
for i in range(2,n):
    c=x+y
    if c==a[i]:
        x=y
        y=c
        flag=1
        continue
    else:
        flag=0
        break
if flag==1:
    print("yes")
else:
    print("no")