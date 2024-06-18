x =input("select an option") # for casting string into integer

match x:
    case "1": 
        print("hello")
    case "2":
        print("namaste")
    case "3":
        print("konichiwa")
    case _:
        print("nothing")    