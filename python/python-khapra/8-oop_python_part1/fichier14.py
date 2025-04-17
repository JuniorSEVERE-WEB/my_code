"""
crate account class with 2 attributes _balance & account no 
create methods for debit, credit &printing the balance


"""
class account: 
  def __init__(self, bal, acc):
    self.balance = bal
    self.account_no = acc

  def debit(self, amount):
    self.balance -= amount
    print(f"apre ou retire {amount} sou kont ou, ou rete  {self.balance}  ")  

  def credit(self, amount):
    self.balance += amount
    print(f" ou mete {amount} sou kont ou, ou vinn gen {self.balance}")  

acc1 = account(10000, 123421)
s1 = acc1.debit(1000)
s2 = acc1.credit(500)    