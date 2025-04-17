"""
private(like) attributes & methods
conceptual implementations in python

private attributes & method are meant to be used only eithin the class and are not
accesible from outside the class
"""

class Account:
  def __init__(self, acc_no, acc_pass):
    self.acc_no = acc_no
    self.acc_pass = acc_pass

acc1 = Account("1234", "abcde")

print(acc1.acc_no)
