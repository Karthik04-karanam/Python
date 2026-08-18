class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
m=Mobile("Samsung","Galaxy S21",70000)
m1=Mobile("Apple","iPhone 13",80000)
print(m.brand,m.model,m.price)
print(m1.brand,m1.model,m1.price)