class Product:
    def __init__(self,productname,price,quantity):
        self.productname=productname
        self.price=price
        self.quantity=quantity
p=Product("Laptop",50000,10)
p1=Product("Mobile",20000,20)
print("Product Name:",p.productname,"Price:",p.price,"Quantity:",p.quantity)
print("Product Name:",p1.productname,"Price:",p1.price,"Quantity:",p1.quantity)