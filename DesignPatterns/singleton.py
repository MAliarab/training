class Singleton(type):
    __inistance = None
    
    def __call__(self, *args, **kwds):
        print("This is call for singleton ...")
        if self.__inistance is None:
            self.__inistance = super().__call__(*args, **kwds)
        return self.__inistance
    
class A(metaclass=Singleton):
    pass    


print(id(A()))
print(id(A()))

