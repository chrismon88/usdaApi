import unittest
from unittest import TestCase
from unittest.mock import patch
import recipes_api

class TESTRECIPESAPI(TestCase):
    
    def test_build_query(self):
        query = recipes_api.build_query('apple', '1122', '3344')
        expected_query = {
            'app_id': '1122',
            'app_key': '3344',
            'type': 'public',
            'q': 'apple'
        }
        self.assertEqual(expected_query, query)


if __name__ == '__main__':
    unittest.main()