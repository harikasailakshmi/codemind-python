a=input()
z=int(a)
while z>9:
    b=list(map(int,a.strip("")))
    if sum(b)>9:
        a=str(sum(b))
    else:
        print(sum(b))
        break
    
