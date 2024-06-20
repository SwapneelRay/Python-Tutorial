def func1():
    x="abc"
    
    def innerfunc1():
        nonlocal x
        x="xyz"
    
    innerfunc1()
    return x

print(func1())