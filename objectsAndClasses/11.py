class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
s=Student("karthik",20,"Python")
s1=Student("Siva",21,"Java")
s2=Student("Ravi",22,"C++")
print("Name:",s.name,"Age:",s.age,"Course:",s.course)
print("Name:",s1.name,"Age:",s1.age,"Course:",s1.course)
print("Name:",s2.name,"Age:",s2.age,"Course:",s2.course)