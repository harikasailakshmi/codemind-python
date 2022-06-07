x=int(input())
z=0
while(x!=0):
    d=x%10
    x=x//10
    if(d>z):
        z=d
print(z)