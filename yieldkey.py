def funcs():
    yield "abc"
    yield 11
    yield 88.7
    
x = funcs()
for i in x:
    print(i)
    

def xyz():
    print("dsa")
    yield 0
    print("not zero")

t=xyz()

for k in t:
    print(k)