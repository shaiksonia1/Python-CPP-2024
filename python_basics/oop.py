class Student:
    def __init__(self,name,age,marks,id):
        self.name = name
        self.age = age
        self.id = id
        self.marks = marks
    
    def __str__(self):
        return 'this is a student class'
    def display(self):
        print('student name : ',self.name)
        print('student age : ',self.age)
        print('student id : ',self.id)
        print('student marks : ',self.marks)

S = [Student('aaa',22,12,56),
     Student('bbb',34,14,36),
    Student('ccc',23,16,66),
    Student('ddd',32,13,26)]

for i in S:
    i.display()

#constructor

class School:
    def __init__(self):
        self.name = 'abc'
        self.roll = 11
        self.marks = 33
        print("in constructor")

    def display(self):
        print(self.name,self.roll,self.marks)

S= School()
S.__init__()

#self parameter

class Employee:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
       

    def display(self):
        print(self.name,self.roll,self.marks)

S= Employee('aaa',23,34)
S.display()


#static and local Variales


class Employee:
    Company = 'Deloitte' # Static variable, shared by all instances of the class
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
       

    def display(self):
        Company = 'Deloitte' # Local variable, exists only inside this method
        print(self.name,self.id,self.salary)
        print("accessing the static variable :", Employee.Company)  # Accessing the static variable
        print("accessing the local variable   :", Company)  # Accessing the local variable

S= Employee('aaa',23,34300)
S.display()