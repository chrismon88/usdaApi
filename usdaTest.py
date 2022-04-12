from unittest import TestCase
from unittest.mock import patch
import usdaApi

class TestUSDAAPI(TestCase):

    def test_build_query(self):
        query = usdaApi.build_query('apple','XpExwpHfydGY8o21Cw1qUGpLvuLlIvsKEgKTirq8')
        expected_query = {
            'query': 'apple',
            'api_key':'XpExwpHfydGY8o21Cw1qUGpLvuLlIvsKEgKTirq8' ,
            'page_size': 2

        }
        self.assertEqual(expected_query, query)

    def test_build_query_raises_exception_no_food(self):
        with self.assertRaises(Exception):
            query = usdaApi.build_query('', 'XpExwpHfydGY8o21Cw1qUGpLvuLlIvsKEgKTirq8')


    @patch('usdaApi.make_api_request', side_efect=[{'foodNutrients':protein}])
    def test_get_nutrition(self, mock_api_request):
            nutrition_data, error= get_food_nutrition('apple')
            expected_nutrition = {'foodNutrients':protein}
            self.assertEqual(expected_nutrition, nutrition_data)
            self.assertIsNone(error)


    @patch('usdaApi.make_api_request', side_efect=[{'foodNutrients':protein}])
    def test_get_nutrition(self, mock_api_request):
         nutrition_data, error = get_food_nutrition('')
         self.assertIsNone(error)