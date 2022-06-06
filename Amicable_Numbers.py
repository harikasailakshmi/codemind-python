x=int(input())
y=int(input())
s=0
k=0
for i in range(1,x):
    if(x%i==0):
        s=s+i
for j in range(1,y):
    if y%j==0:
        k=k+j
if k==x and s==y:
    print("Amicable")
else:
    print("Not Amicable")