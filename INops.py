list1 =[1,5,2,4,6,8,9]
list2 =[8,9,10,11,12,15]

for item in list1:
    if item not in list2:
        print(item,"not present in both list")
    else:
        print(item,"present in both list")
        