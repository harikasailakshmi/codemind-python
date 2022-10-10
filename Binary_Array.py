n=int(input())
a=list(map(int,input().split()))
z=1
for i in a:
    if i!=0 and i!=1:
        z=0
        break
if z==0:
    print("False")
else:
    print("True")