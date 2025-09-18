class stud:
    def __init__(self,x,y,z):
        self.rollnum=x
        self.name=y
        self.dept=z
    def display(self):
        print("student rollnumber:",self.rollnum)
        print("student name:",self.name)
        print("student department:",self.dept)
x=int(input("Enter roll number:"))
y=input("Enter a name:")
z=input("Enter the department:")
obj=stud(x,y,z)
obj.display()
