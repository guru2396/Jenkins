#!/usr/bin/python3

import unittest
from Prog1 import summation

class TestSum(unittest.TestCase):
	def test(self):
		data=[10,12]
		res=summation(data)
		self.assertEqual(res,22)

if __name__=='__main__':
	unittest.main()
