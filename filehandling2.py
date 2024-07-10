file_handler= open("assignment.txt","r+")

print(file_handler.tell())

file_handler.seek(250)

print(file_handler.tell())

file_handler.seek(20)
print(file_handler.tell())
print(file_handler.read())
