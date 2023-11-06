import csv
class Item:
    
    discount=.10
    all =[]
    def __init__(self,name: str,price : float,quantity=0): 
        #Validations
        assert price >=0 , f"Price {price} is negative"
        assert quantity >=0, f"Quantity {quantity} is negative"

        print(f"this is {name}")
        self.__name=name
        self.__price=price
        self.quantity=quantity

        #execute
        Item.all.append(self)

    #getter
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    #setter
    @name.setter
    def name(self,value):
        self.__name=value
    
    def apply_increment(self,increment_val):
        self.__price=self.__price + self.__price * increment_val


    def __repr__(self) : # represent instances
        return f"{self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}')"

    def display(self): #self -> this object
        # print(x,y)
        print(self.name,self.quantity,self.__price) #access this methods
        print(self.name,Item.discount) #access this methods
        pass
    
    def apply_dicount(self):
        self.__price=self.__price * self.discount
        print(self.__price)
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as file:
            reader=csv.DictReader(file)
            items=list(reader)

        for item in items:
            Item (
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        
        elif isinstance(num,int):
            return True

    # private method
    def __private_method(self):
        pass