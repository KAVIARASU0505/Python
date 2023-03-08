def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        raise ValueError("Cannot divide by zero")
    return x/y
def com(x,y):
    if x<y:
      return x
def nq(x,y):
    if x==y:
      return print("Equal")
import unittest
class Dummy:
  x = 5
class TestMethods(unittest.TestCase):
    def test_check(self):
        firstValue = Dummy()
        secondValue = firstValue
        message = "The output is false"
        self.assertIs(firstValue, secondValue, message)
  
if __name__ == '__main__':
    unittest.main()