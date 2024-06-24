def sum(*args):
    total=0
    for x in args:
        total = total+ x
        
    return total


print(sum(1,5,4,3))
print(sum(1,6))