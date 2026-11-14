import unittest
from calc import add, divide

class TestCalculator(unittest.TestCase):
    def test_assert_equal(self):
        actual = add(2, 3) 
        expected = 5
        self.assertEqual(actual, expected)

    def test_assert_true(self):
        result = add(2, 3) == 5
        self.assertTrue(result)
        
    def test_assert_in(self):
        results = [add(2, 3), add(4, 5), add(10, 2)]
        self.assertIn(5, results)
        
    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
            
    def test_divide_normal_values(self):
        self.assertEqual(add(2,3), 5)
        
if __name__ == "__main__":
    unittest.main()