class Employee:

    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal

    @classmethod
    def stringdot(cls,str):
        return cls(str.split('.')[0],str.split('.')[1],str.split('.')[2])

    @classmethod
    def stringdash(cls,string):
        name,age,sal=string.split('_')
        return cls(name,age,sal)

    def info(self):
        print(f"Emplyee Name is {self.name} his age is {self.age} and Salary {self.sal}.")

e1=Employee("Aryakumar",22,25000)
e1.info()


str2="Aayushkumar.19.49000"
e2=Employee.stringdot(str2)
e2.info()


str3="SarahKhan_21_46000"
e3=Employee.stringdash(str3)
e3.info()
