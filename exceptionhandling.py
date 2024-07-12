
#divide by zero error

a=50
b=0
try:
    print(a/b)
except IndexError:
    print("index out of bounds")
except ZeroDivisionError:
    print("you should not divide by zero")
    
finally:
    print("your calculations are complete")
print("after division result continue this program")