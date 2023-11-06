'''
        constructors - init
        default constructor is called automatically
        parameterized ->use default parameters for >1 constructors 
        use :  type
'''
    
    
'''attributes - 
        set in constructors
        add extra as well with objects

        self.attribute //access
'''

'''
    class attributes
    in the class and object accessible
    priority: instance level -> class level 
    __dict__ -> attributes
    can have separate and unique class level atrributes value

    @classmethod decorator  - manimpulate different structures (instantiation)
    def name(cls):
    

    call from instance & class
'''

''' 
    static methods -> related to only class -> not unique for instance
    @staticmethod
    def name():
    call from instance & class
'''

'''
    set __init__ 
        self._readOnly
        self.__private
    @property
    def actual(self):
        return self._hidden
'''



# item1=Item("abc",100,5) #create instance
# item2=Item("def",100,5) #create instance
# item1.discount=.20
# item1.apply_dicount()
# item2.apply_dicount()


# print(item1.__dict__)
# print(Item.__dict__)

# print(Item.all)
# for instance in Item.all:
#     print(instance.name)


# Item.instantiate_from_csv()

# print(Item.is_integer(4.0))


'''
    Inheretence - 
    constructors are inhereted
    methods are inhereted
    super function call to base class (all methods and functions become accessible)
    child is an instance of base
'''



from Item import Item
from Phone import Phone



# phone1=Phone("phone1",500,2,40)
# phone2=Item("phone2",500,2)
# print(Phone.all)
# print(Item.all) 


item1=Item("car",500,1)
print(item1.name)
# item1.name="g" #error
item1.name="bike" # after name setter
print(item1.name)


#encapsulation
item1.apply_increment(0.2)
print(item1.price)






