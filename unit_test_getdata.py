import os
import unittest
import urllib3
from my_function import get_data
import warnings
warnings.filterwarnings('ignore')

url = "https://data.seattle.gov/resource/4xy5-26gy.csv"
filename = "4xy5-26gy.csv"
wrong_url = "https://data.seattle/resource"

class GetDataTestCase(unittest.TestCase):
    # case: (a) file is present locally
    def test_file_exist(self):
        if os.path.exists(filename) is False:
            get_data(url)
        self.assertEqual(get_data(url), None)
        os.remove(filename)

    # case: (b) file is not present locally, and the URL points to a file that exists
    def test_file_not_exist(self):
        if os.path.exists(filename):
            os.remove(filename)
        self.assertTrue(get_data(url))

    # case: (c) URL does not point to a file that exists
    def test_invalid_url(self):
        if os.path.exists(filename):
            os.remove(filename)
        url = "https://data.seattle/resource"
        with self.assertRaises(ValueError) as context:
            get_data(wrong_url)
        self.assertTrue('URL is not valid' in str(context.exception))

if __name__ == '__main__':
    unittest.main()