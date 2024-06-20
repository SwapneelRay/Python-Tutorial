#non-tail recursion

def recurfunction(n):
    if(n==0):
        return 1
    
    return n * recurfunction(n-1)

print(recurfunction(6)) # 6*5*4*3*2*1


#tail recusion

def recur_function(n,a=1):
    if(n==0):
        return a
    
    return recur_function(n-1,n*a)

print(recur_function(6))