x=int(input())
temp=x
z=x*x
c=0
while x>0:
    d=x%10
    x=x//10
    c+=1
v=0
w=0
while z>0 and c>0:
    d=z%10
    z=z//10
    c-=1
    v=v*10+d
while v!=0:
    d=v%10
    v=v//10
    w=w*10+d
if(w==temp):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")