
Classrecords = {
    "student1":{
        "Name":"xyz",
        "age":15,
        "hobby":"guitar"
    },
    "student2":{
        "Name":"abc",
        "age":14,
        "house":"sun"
    },
    "student3":{
        "Name":"def",
        "age":13,
        "location":"delhi"
    },
    "student4":{
        "Name":"ghi",
        "age":13
    }
}

for x,y in Classrecords.items():
  for j in y:
    print(j,y[j] )