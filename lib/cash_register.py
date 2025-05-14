#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount=discount
    self.total = 0
    self.items =[]
    self.last_transaction_amount = 0
    
  def add_item(self, title, price, quantity=1):
      for _ in range(quantity):
          self.items.append(title)
      self.total += price * quantity
      self.last_transaction_amount = price * quantity
  
  def apply_discount(self):
    if self.discount:
     self.total = self.total * (1 - self.discount / 100)
     print(f"After the discount, the total comes to $800.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
        self.total -= self.last_transaction_amount
  
    
    
  pass
