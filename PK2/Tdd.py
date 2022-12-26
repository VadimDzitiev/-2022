import unittest
from main1 import *

task1_result = [('Иванов', 'Исторический оркестр'), ('Петров', 'Симфонический оркестр'), ('Свиридов', 'Симфонический оркестр'), ('Слепаков', 'Духовой оркестр')]

task2_result = [('Исторический оркестр', 40000), ('Духовой оркестр', 34500), ('Симфонический оркестр', 23500)]

task3_result = ['Исторический оркестр', 'Иванов', 'Багаев']

class TestEquation(unittest.TestCase):
	def test_check_task1(self):
		self.assertEqual(task1_result, N1())

	def test_check_task2(self):
		self.assertEqual(task2_result, N2())

	def test_check_task3(self):
		self.assertEqual(task3_result, N3())

if __name__ == '__main__':
	unittest.main()