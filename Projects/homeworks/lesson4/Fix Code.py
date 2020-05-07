#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson4\Fix Code.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson4
# Created Date: Saturday, April 18th 2020, 9:09:28 am
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

class Phone:
  def __init__(self, phone_number):
    self.number = phone_number

  def call(self, other_number):
    print("Calling from", self.number, "to", other_number)

  def text(self, other_number, msg):
    print("Sending text from", self.number, "to", other_number)
    print(msg)

new_phone = Phone(5214)
test_phone = Phone(5214)
test_phone.call(515)
test_phone.text(int(141), "Hi!")