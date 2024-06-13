Dict1 ={
    # "Key": "Value"
    "Name":"xyz",
    "Age":24,
    "Salary":55555,
    "Surname": "abc"
    
}

# print(Dict1)
# print(type(Dict1))
# Dict1["Name"] = "xyz"



print(len(Dict1))

# for x in Dict1:
#     print(x +":",end="")
#     print(Dict1[x])
    
for x, y in Dict1.items():
  print(x, y)
    
del Dict1["Age"]
print(Dict1)
