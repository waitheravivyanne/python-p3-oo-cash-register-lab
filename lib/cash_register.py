#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

  def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

  def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

  def void_last_transaction(self):
        if self.items:
            last_item_price = 0
            for title in reversed(self.items):
                if title != self.items[-1]:
                    last_item_price = self.total - last_item_price
                    break
                last_item_price += self.total / len(self.items)
                self.items.pop()
            self.total -= last_item_price







