class Person(object):
    
    def __init__(self,name, id):
        self.name=name
        self.id=id
    def display(self):
        print("the person name is {} and the personid is {}".format(self.name,self.id))

class emp(Person):

    def __init__(self,name,id,empid):
        self.empid=empid
        Person.__init__(self,name,id)

obj1=Person("shani",456)
obj1.display()

obj2=emp("aman",457,50047)
obj2.display()

