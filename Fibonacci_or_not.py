x=int(input())
a=0
b=1
c=0
for i in range(1,x+1):
    c=a+b
    if c==x:
        print("True")
        break
    elif c>x:
        print("False")
        break
    a=b
    b=c