class school:
    name=""
    address=""

    def __init__(self,name,address):
        self.name=name
        self.address=address

    def teacher(self,name,subject):
        self.name=name
        self.subject=subject
    def students(self,name , classe):
        print(name,classe)

    def school_func(self):
        print("The School name is {} and the address is {}".format(self.name,self.address))


school1=school(" Rana public high school ","Bangalore")
school1.school_func()
school1.students("shani","maths")