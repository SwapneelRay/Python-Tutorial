
def recursion(n):
    if n<=1:
        return n
    else:
        return(recursion(n-1)+recursion(n-2))
    
terms = int(input("number of terms"))
for i in range(terms):
    print(recursion(i))
    
    
    