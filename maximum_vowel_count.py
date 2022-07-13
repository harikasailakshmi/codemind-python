x=input()
c=0
s=0
z=0
for i in range(len(x)):
    if x[i]==" ":
        z+=1
        if s>c:
            c=s
        s=0
    elif x[i] in 'aeiouAEIOU':
        s+=1
    else:
        continue
if(z==0):
    print(s)
else:
    print(c)