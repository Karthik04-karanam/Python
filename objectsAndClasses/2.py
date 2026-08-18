class Car:
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
s1=Car("BMW","BMW",1000000)
s2=Car("Audi","Audi",2000000)
s3=Car("Benz","Benz",3000000)

print(s1.name,s1.brand,s1.price)
print(s2.name,s2.brand,s2.price)
print(s3.name,s3.brand,s3.price)
   