#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            if not hasattr(self, '_discount'):
                self._discount = 0

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self._previous_transactions.append({"item": item, "price": price, "quantity": quantity})

    def apply_discount(self):
        if self.discount <= 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # The test expects a specific message format
            # Converting to int if it's a whole number to match tests ($800 vs $800.0)
            display_total = int(self.total) if self.total == int(self.total) else self.total
            print(f"After the discount, the total comes to ${display_total}.")

    def void_last_transaction(self):
        if not self._previous_transactions:
            print("There is no transaction to void.")
        else:
            last = self._previous_transactions.pop()
            self.total -= last["price"] * last["quantity"]
            # Remove the items added by this transaction
            for _ in range(last["quantity"]):
                if last["item"] in self.items:
                    self.items.remove(last["item"])
