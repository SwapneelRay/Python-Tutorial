def sum(*args):#*args non keyword variable parameter
    total=0
    for x in args:
        total = total+ x
        
    return total


print(sum(1,5,4,3))
print(sum(1,6))


def studentdata(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
        

studentdata(name="xyz",standard="12th",hobby="cricket")
studentdata(name="abc",standard="10th",hobby="guitar",address="delhi")
