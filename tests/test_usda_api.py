from unittest import TestCase
from unittest.mock import patch 
import usdaApi


class TestUSDAAPI(TestCase):



    def test_build_query(self):
        query = usdaApi.build_query('cheese', '123456')
        expected_query = {
            'query': 'cheese',
            'api_key': '123456',
            'pageSize': 2
        }
        self.assertEqual(expected_query, query)


    def test_build_query_raises_exception_no_food(self):
        with self.assertRaises(Exception):
            query = usdaApi.build_query('', '123456')
    

    # high-level - making the api call 
    # testing the get_food_nutrition function

    # test we get nutrition data for a valid food 

    # what if food not found?

    # what if api returns error? 

    # what if can't connect to api? 

# happy path - things working 
    @patch('usdaApi.make_api_request', side_effect=[{'calories': 100}])
    def test_get_nutrition(self, mock_api_request):
        nutrition_data, error = get_food_nutrition('apple')
        expected_nutrition = { 'calories': 100, 'sugar': 4}
        self.assertEqual(expected_nutrition, nutrition_data)
        self.assertIsNone(error)


    @patch('usdaApi.make_api_request', side_effect=[{'calories': 100}])
    def test_get_nutrition(self, mock_api_request):
        nutrition_data, error = get_food_nutrition('')
        self.assertIsNotNone(error)
    
