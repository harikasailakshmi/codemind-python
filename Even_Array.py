n=int(input())
a=list(map(int,input().split()))
z=0
for i in a:
    if i%2!=0:
        z=1
if z==0:
    print("True")
else:
    print("False")