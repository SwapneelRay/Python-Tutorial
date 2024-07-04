list1 = [5,4,11,88,44,6,3]
list2=[1,2,3,4,5,6]
print(list1)
listlambda = list(map(lambda i:i+1,list1))

print(listlambda)


def adder(i):
    if i<10:
        return i+1
    else:
        return i-100

listfunc = list(map(adder,listlambda))
print(listfunc)

print(list1)
print(list2)

listres= list(map(lambda x,y: x+y,list1,list2))

print(listres)
