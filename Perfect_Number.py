a=int(input())
c=0
for i in range(1,a):
    if a%i==0:
        c+=i
j=(a==c)
print(j if "True" else "False")