file_handler= open("assignment.txt","r+")
file_handler2=open("assignment1.txt","w+")

print(file_handler.name)
print(file_handler.mode)
print(file_handler.closed)

assignment_data=file_handler.read()

#print(assignment_data)
file_handler2.write(assignment_data)

print(file_handler.seek())


file_handler.close() # always close file

