#implicit type conversion

a=5
b= 11.6

print("a is of type",type(a))
print("b is of type",type(b))

a = b/a

print("a is of type",type(a))

#explicit type conversion
x="100101" # 37
a=int(x,2)
print("a is of type",type(a))
a= float(a)

print("x is of type",type(x))
print("a is of type",a,type(a))

a = b/a

print("a is of type",type(a))