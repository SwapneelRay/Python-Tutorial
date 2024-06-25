#with return and argument
def exchange(x,y):
    x,y=y,x
    return x,y

a=5
b=8
print("a =",a)
print("b =",b)

a,b=exchange(a,b)

print("a after exchange =",a)
print("b after exchange =",b)

#without return and arg

def change():
    a1=51
    b1=81
    print("a =",a1)
    print("b =",b1)
    
    a1,b1=b1,a1
    print("a after exchange =",a1)
    print("b after exchange =",b1)
    
change()