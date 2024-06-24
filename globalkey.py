def func():
    global x
    x = "local"
    print(x)
    

func()

print(x)