class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
e=Employee("John","IT",50000)
e1=Employee("Alice","HR",60000)
e2=Employee("Bob","Finance",70000)
e3=Employee("Eve","Marketing",80000)
e4=Employee("Charlie","Sales",90000)
print("Name:",e.name,"Department:",e.department,"Salary:",e.salary)
print("Name:",e1.name,"Department:",e1.department,"Salary:",e1.salary)
print("Name:",e2.name,"Department:",e2.department,"Salary:",e2.salary)
print("Name:",e3.name,"Department:",e3.department,"Salary:",e3.salary)
print("Name:",e4.name,"Department:",e4.department,"Salary:",e4.salary)
