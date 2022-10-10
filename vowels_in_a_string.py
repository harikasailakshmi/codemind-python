n=input()
a=list(n)
k=input()
if k in a:
    print("True")
    print(a.index(k))
else:
    print("False")