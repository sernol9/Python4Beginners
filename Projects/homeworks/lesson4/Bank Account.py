#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson4\Bank Account.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson4
# Created Date: Saturday, April 18th 2020, 9:23:46 am
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sat Apr 18 2020
# Modified By: Olivia Serna
# -----
# Copyright (c) 2020 OLI CO. LTD.
# 
# Know thy self, know thy enemy. A thousand battles, a thousand victories
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###

class BankAccount:
  def __init__(self):
    self.balance = 0

  def deposit(self, amount):
      self.balance += amount

  def withdraw(self, amount):
      self.balance -= amount

class BankAccountOverdraft (BankAccount):
    def __init__(self):
        super().__init__
        self.overdraft_fees = 0

    def withdraw(self, amount):
        super().withdraw(amount)
        self.overdraft_fees = (self.overdraft_fees + 20 if self.balance < 0 else 0)

dbs1 = BankAccountOverdraft()
dbs1.deposit(100)
print(dbs1.balance)  # -> prints 100
dbs1.withdraw(200)
print(dbs1.balance)  # -> prints -100
print(dbs1.overdraft_fees)  # -> prints 20

