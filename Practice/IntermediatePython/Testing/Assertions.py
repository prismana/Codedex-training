import unittest

def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def is_capitalized(s):
    return s[0].isupper()

class TestStringUtils(unittest.TestCase):
    def test_reverse(self):
        result = reverse_string("Prismana")

        self.assertEqual(result, "anamsirP")

    def test_capital(self):
        result = capitalize_string("Prismana")

        self.assertEqual(result, "anamsirP")
    
    def test_isCapitalize(self):
        result = is_capitalized("Prismana")

        self.assertTrue("Prismana" in result)


if __name__ == '__main__':
    unittest.main()