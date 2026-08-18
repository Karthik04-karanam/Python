class Laptop:
    def __init__(self,brand,RAM,processor,price):
        self.brand=brand
        self.RAM=RAM
        self.processor=processor
        self.price=price
l1=Laptop("Dell","8GB","i5",50000)
l2=Laptop("HP","16GB","i7",70000)
print("Brand:",l1.brand,"RAM:",l1.RAM,"Processor:",l1.processor,"Price:",l1.price)
print("Brand:",l2.brand,"RAM:",l2.RAM,"Processor:",l2.processor,"Price:",l2.price)