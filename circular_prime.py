def prime(a):
    if a==0 or a==1:
        return 0
    for i in range (2,a):
        if a%i==0:
            return 0
    return 1
n=input()
k=int(n)
r=int(n[::-1])
if prime(k)==1 and prime(r)==1 :
    print("circular prime")
elif prime(k)!=1:
    print("not prime")
else:
    print("prime but not a circular prime")
