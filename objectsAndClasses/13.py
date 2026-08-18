class Product:
    def __init__(self,productname,price,quantity):
        self.productname=productname
        self.price=price
        self.quantity=quantity
p=Product("Laptop",50000,10)
c=p.price*p.quantity
print(c)
    