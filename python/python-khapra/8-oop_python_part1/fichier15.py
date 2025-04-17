"""
crate account class with 2 attributes _balance & account no 
create methods for debit, credit &printing the balance

"""

class account:
  def __init__(self, bal, acc):
    self.balance = bal
    self.account_no = acc

  def debit(self, amount):
    print(f"montant kob ou a se {self.balance}, ou retire {amount} ladan ki vinn fe ")
    self.balance -= amount
    print(f"balance ou se : {self.get_balance()}")

  def credit(self, amount):
    print(f"montant kob ou a se {self.balance}, ou mete {amount} ladan ki vinn fe ")
    self.balance += amount
    print(f"balance ou se : {self.get_balance()}")  

  def get_balance(self):
    return self.balance  

acc1 = account(10000, 444)
acc1.debit(1000)
acc1.credit(500)