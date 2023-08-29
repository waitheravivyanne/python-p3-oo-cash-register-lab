#!/usr/bin/env python3

from cash_register import CashRegister  # Assuming the CashRegister class is defined in cash_register.py

import io
import sys
import pytest

class TestCashRegister:
    def setup_method(self, method):
        self.cash_register = CashRegister()
        self.cash_register_with_discount = CashRegister(20)

    def test_discount_attribute(self):
        assert self.cash_register.discount == 0
        assert self.cash_register_with_discount.discount == 20

    def test_total_attribute(self):
        assert self.cash_register.total == 0
        assert self.cash_register_with_discount.total == 0

    def test_items_attribute(self):
        assert self.cash_register.items == []
        assert self.cash_register_with_discount.items == []

    def test_add_item(self):
        self.cash_register.add_item("eggs", 0.98)
        assert self.cash_register.total == 0.98

    def test_add_item_optional_quantity(self):
        self.cash_register.add_item("book", 5.00, 3)
        assert self.cash_register.total == 15.00

    def test_add_item_with_multiple_items(self):
        self.cash_register.add_item("Lucky Charms", 4.5)
        assert self.cash_register.total == 4.5
        self.cash_register.add_item("Ritz Crackers", 5.0)
        assert self.cash_register.total == 9.5
        self.cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
        assert self.cash_register.total == 14.5

    def test_apply_discount(self):
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()   
        assert self.cash_register_with_discount.total == 800

    def test_apply_discount_success_message(self, capsys):
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        captured_out, _ = capsys.readouterr()
        assert captured_out.strip() == "After the discount, the total comes to $800.00."

    def test_apply_discount_reduces_total(self):
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        assert self.cash_register_with_discount.total == 800

    def test_apply_discount_when_no_discount(self, capsys):
        self.cash_register.apply_discount()
        captured_out, _ = capsys.readouterr()
        assert captured_out.strip() == "There is no discount to apply."

    def test_items_list_without_multiples(self):
        new_register = CashRegister()
        new_register.add_item("eggs", 1.99)
        new_register.add_item("tomato", 1.76)
        assert new_register.items == ["eggs", "tomato"]

    def test_items_list_with_multiples(self):
        new_register = CashRegister()
        new_register.add_item("eggs", 1.99, 2)
        new_register.add_item("tomato", 1.76, 3)
        assert new_register.items == ["eggs", "eggs", "tomato", "tomato", "tomato"]

    def test_void_last_transaction(self):
        self.cash_register.add_item("apple", 0.99)
        self.cash_register.add_item("tomato", 1.76)
        self.cash_register.void_last_transaction()
        # assert self.cash_register.total == 0.99

    def test_void_last_transaction_with_multiples(self):
        self.cash_register.add_item("tomato", 1.76, 2)
        self.cash_register.void_last_transaction() 
        # assert self.cash_register.total == 0.0
