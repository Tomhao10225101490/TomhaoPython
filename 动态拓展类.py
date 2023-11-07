from types import MethodType
class Student:
    pass
def SetName(self, name):
    self.name = name
def SetSno(self, sno):
    self.sno = sno
if __name__ == '__main__':
    stu1 = Student()
    stu2 = Student()
    stu1.SetName = MethodType(SetName, stu1)#仅仅给stu1绑上了SetName，别的实例没有
    Student.SetSno = SetSno#给整个类都绑上了SetSno，都可以用
    stu1.SetName("Tom")
    stu1.SetSno('10086')
    # stu2.SetName('Mike')
    stu2.SetSno('10088')
    print(stu1.name)
    print(stu1.sno)
    # print(stu2.name)
    print(stu2.sno)

################################################################
class Person:
    __slots__ = ('name')#定义允许动态拓展的属性
class Student(Person):
    __slots__ = ('sno')
class Postgraduate(Student):
    pass
if __name__ == '__main__':
    stu = Student()
    stu.sno = '1810100'
    stu.name = 'Bob'
    pg = Postgraduate()
    pg.sno = '190900'
    pg.name = 'mIke'
    pg.tutor = 'zhong'
    print(pg.tutor)