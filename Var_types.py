#protected _a

class new(object):
    
    def __init__(self):
        self._protected_var=89
    

class dup(new):
    def __init__(self):
        new.__init__(self)
        print( "the main protected var ={}".format(self._protected_var))
        
        self._protected_var=9
        print("the derived protected var ={}".format(self._protected_var))

   




obj1=new()
obj2=dup()


#private__a