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
        print(self.name, self.classe)
    def school_func(self):
        print("The School name is {} and the address is {}".format(self.name,self.address))


school1=school(" Rana public high school ","Bangalore")