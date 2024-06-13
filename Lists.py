list1 = [1,15.9,"python","xyz",2]
list2 = [1,2,"python","xyz",15.9]
print(list1[3])
print(type(list1[3]))

print(list1==list2)

#functions on list 
#indexing
#splitting

print(list1[1:5])

list3 = list1[1:5]

#steps
listall=[1,2,3,4,5,6,7,8,9,10,11,12,13]
listeven= listall[1::2]
listodd= listall[0::2]

print(listeven)
print(listodd)

#negative indexing
print(listall[-5:-2])


list1[2:4]=["java","abc"]
list1.insert(0,25)
print(list1)
list1.remove(25)
print(list1)