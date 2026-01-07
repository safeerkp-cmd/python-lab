class bank:
    def __init__(self,accno,name,typeofacc,balance):
        self.accno=accno
        self.name=name
        self.typeofacc=typeofacc
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount >= amount:
            self.balance-=amount
        else:
            print("no balance")
    def display(self):
        print("Account No:", self.accno)
        print("Name:", self.name)
        print("Account Type:", self.typeofacc)
        print("Balance:", self.balance)
dep=int(input("enter amount for deposit"))
wit=int(input("enter amount for withdraw"))

bnk=bank(1032,"safeer","saving",1000)
bnk.deposit(dep)
bnk.withdraw(wit)
bnk.display()
        
