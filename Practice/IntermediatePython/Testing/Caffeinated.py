import unittest

class CoffeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

# Test case
class TestCoffeMenu(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    

# Run
if __name__ == "__main__":
    unittest.main