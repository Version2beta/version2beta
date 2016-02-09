from cart import Cart
import unittest
from expecter import expect

class TestCart(object):
  def test_add(self):
    expect(Cart.add([], {'name': 'item'})) == [('add', {'name': 'item'})] 
