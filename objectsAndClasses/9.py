class BankAccount:
    def __init__(self,accountNumber,accountHolderName):
        self.accountNumber=accountNumber
        self.accountHolderName=accountHolderName
b=BankAccount("1234567890","karthik")
b1=BankAccount("0987654321","Siva")
print("Account Number:",b.accountNumber,"Account Holder Name:",b.accountHolderName)
print("Account Number:",b1.accountNumber,"Account Holder Name:",b1.accountHolderName)
