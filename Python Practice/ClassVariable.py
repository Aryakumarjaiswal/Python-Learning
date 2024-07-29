class Preparation:
    Aim="DataScientist"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def ClassVariableChange(self,NewName):
        self.Aim=NewName
    
    def intro(self):
        print(f"I'm {self.name} my age is {self.age} and I Promise to become DataScientist")

Aryan=Preparation("Aryakumar",22)
Aryan.intro()
print(Aryan.Aim)
print(Preparation.Aim)

Ayush=Preparation("Ayushkumar",22)

Ayush.ClassVariableChange("Google Data Scientist")

print(Aryan.Aim)
print(Preparation.Aim)
