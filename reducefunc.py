import functools
list1 = [5,4,11,88,44,6,3]

listlamda= functools.reduce(lambda result,value: result+value,list1)

print(listlamda)

print("total=",sum(list1))