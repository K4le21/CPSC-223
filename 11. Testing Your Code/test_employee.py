import unittest
from employee import Employee

class testMethod(unittest.TestCase):
    def setUp(self):
        self.new_Employee = Employee("John", "Doe")

    def test_give_default_raise(self):
        self.new_Employee.give_raise()

    def test_give_custom_raise(self):
        self.new_Employee.give_raise(10000)



if __name__ == '__main__':
    unittest.main() 