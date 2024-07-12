list1=[1,2,3,5,1]
d_list= list1.copy()
list1.reverse()

print(d_list)
print(list1)


if(list1==d_list):
    print("is pallindrome")
else:
    print("not a pallindrome")