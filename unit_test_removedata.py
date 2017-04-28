import os
import unittest
from my_function import remove_data

filename = "4xy5-26gy.csv"

class RemoveDataTestCase(unittest.TestCase):
    # case: (a) file is present locally
    def test(self):
        if os.path.exists(filename):
            self.assertTrue(remove_data(filename))
        else:
            with self.assertRaises(ValueError) as context:
                remove_data(filename)
            self.assertTrue('File does not exist.' in str(context.exception))

if __name__ == '__main__':
    unittest.main()