from Item import Item
class Phone (Item):
    # all=[]
    discount = 0.3 # over ride
    def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
        #call to super
        super().__init__(
            name,price,quantity
        )
        #Validations
        assert broken_phones >=0, f"Quantity {broken_phones} is negative"

        #assign
        print(f"this is {name}")
        self.broken_phones=broken_phones

        #execute
        # Phone.all.append(self)

