import pickle



class Employee:
    def __init__(self,name,salary,emp_code):
        self.name=name
        self.salary= salary
        self.emp_code=emp_code
        
    def display(self):
        print(f'Name={self.name} Salary={self.salary } Employee Id ={self.emp_code}')
    
with open('employee.dat', mode='ab') as file:
    emp1 = Employee('Swapneel',50000,'002')
   
    pickle.dump(emp1,file) # pickling
   
    
with open('employee.dat',mode='rb') as file1:
    var= pickle.load(file1) # unpickling
    print(var.salary)



            