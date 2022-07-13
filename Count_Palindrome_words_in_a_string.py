x=input()
x=x.lower()
x=x.split()
k=0
for i in x:
    z=i[::-1]
    if(i==z):
        k+=1
    else:
        continue
print(k)