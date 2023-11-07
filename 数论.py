class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def __init__(self,fname,lname,stuno):
        Person.__init__(self,fname,lname)
        self.stuno = stuno
    def printname2(self):
        print(self.firstname,self.lastname,self.stuno)

s1 = Student("Elon","Musk","001")
print(s1.firstname)
print(s1.lastname)
print(s1.stuno)
s1.printname();
s1.printname2();