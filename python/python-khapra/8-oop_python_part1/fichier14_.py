class account:
  def __init__(self, bal, acc):
    self.balance = bal
    self.account_no = acc

    #debit method
  def debit(self, amount):
    self.balance -= amount
    print(f" Rs. {amount} was debitted")
    print(f"Total balance = ", self.get_balanced())
  
  def credit(self, amount):
    self.balance += amount
    print(f" Rs. {amount} was credited")
    print(f"Total balance = ", self.get_balanced())
    
  def get_balanced(self):
    return self.balance  

acc1 = account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)