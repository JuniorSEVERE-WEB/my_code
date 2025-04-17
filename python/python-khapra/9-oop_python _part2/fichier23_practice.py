"""
Create a class called order which 
stores item & its price.
Use Dunder function__gt__() to convey that:
order1 > order2 if price of order > price of order2

"""
class Order:
  def __init__(self, item, price):
    self.item = item 
    self.price = price

  def __gt__(self, odr2):
    return self.price > odr2.price  



odr1 = Order("chips", 20)
odr2 = Order("tea", 15)
