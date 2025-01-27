#define class
class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.acc_no=acc
#debit method
    def debit(self,amount):
        self.balance -=amount
        print("rs",amount,"was debit")
        print("tatal balance=",self.get_balance())
#credit method
    def credit(self,amount):
        self.balance +=amount
        print("rs",amount,"was credit")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=account(12000,12456)
print(acc1.balance)
print(acc1.acc_no)
acc1.debit(500)
acc1.credit(20000)
acc1.credit(50000)