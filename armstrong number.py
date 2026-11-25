def aa(a,v=0):
    if a == 0:
        return v 
    e=a%10
    v=v+(e**s)
    return aa(a//10,v)

n=int(input("enter: "))
s=len(str(n))
p=aa(a=n)
if n == p:
    print(f"{n} is an armstrong number" )
else:
    print(f"{n} is not an armstrog number") 
    