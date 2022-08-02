#protected _a

class new(object):
    
    def __init__(self):
        self._protected_var=89
    
    def display(self):
        print("the value of protected in main class {}".format(self._protected_var))
    

class dup(new):
    def __init__(self):
        
        new.__init__(self)
        self._protected_var=9

   




obj2=new()
obj2.display()

#private__a