# import unittest

# # Function to be tested
# def subtract(x, y):
#     return x - y

# # Test case for the subtract function
# class TestSubtractFunction(unittest.TestCase):
    
#     def test_subtract_integers(self):
#         self.assertEqual(subtract(10, 5), 5)
    
#     def test_subtract_floats(self):
#         self.assertAlmostEqual(subtract(5.5, 2.3), 3.2)
    
#     def test_subtract_negative(self):
#         self.assertEqual(subtract(-1, -1), 0)

# if __name__ == '__main__':
#     unittest.main()


import unittest

# Function to be tested
def add(x, y):
    return x + y

# Test case for the add function
class TestAddFunction(unittest.TestCase):
    
    def test_add_integers(self):
        self.assertEqual(add(3, 3), 5)
    
    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.2), 5.7)

# Custom runner to check if any tests fail
def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAddFunction)
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    print("result:",result.wasSuccessful())
    # Return False if there were any failures or errors
    return not result.wasSuccessful()

if __name__ == '__main__':
    test_failed = run_tests()
    print(f'test_failed:',test_failed)
    if run_tests():
        print("Some tests failed.")
    else:
        print("All tests passed.")
