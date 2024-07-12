import pickle
import employee

var = employee.Employee('xyz',50,'002')

with open('employee.dat',mode='rb') as file1:
    var= pickle.load(file1) # unpickling
    var.display()