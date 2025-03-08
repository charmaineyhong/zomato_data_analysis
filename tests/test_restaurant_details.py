import unittest
from unittest.mock import patch
import pandas as pd
from src.restaurant_details import process_restaurant_details

class TestRestaurantDetails(unittest.TestCase):
    def setUp(self):
        self.mock_restaurants = pd.DataFrame({
            'Restaurant Id': [1, 2],
            'Restaurant Name': ['Restaurant A', 'Restaurant B'],
            'Country': ['USA', 'Canada'],
            'City': ['New York', 'Toronto'],
            'User Rating Votes': [200, None],  
            'User Aggregate Rating': [4.5, 4.0],
            'Cuisines': ['Mexican', 'Chinese'],
            'Event Date': ['2025-03-01', '2025-03-02']
        })

        self.mock_country_codes = pd.DataFrame({
            'Country': ['USA'],
            'Code': ['US']
        })

    @patch('pandas.read_excel', return_value=pd.DataFrame({'Country': ['USA'], 'Code': ['US']}))
    @patch('pandas.read_json', return_value=pd.DataFrame({
        'Restaurant Id': [1, 2],
        'Restaurant Name': ['Restaurant A', 'Restaurant B'],
        'Country': ['USA', 'USA'],
        'City': ['Los Angeles', 'San Francisco'],
        'User Rating Votes': [200, None],
        'User Aggregate Rating': [4.5, 4.0],
        'Cuisines': ['Mexican', 'Chinese'],
        'Event Date': ['2025-03-01', '2025-03-02']
    }))
    def test_handle_missing_data(self, mock_read_json, mock_read_excel):
        result = process_restaurant_details()
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.loc[1, 'User Rating Votes'], 'NA')

    @patch('pandas.read_excel', return_value=pd.DataFrame({'Country': ['USA'], 'Code': ['US']}))
    @patch('pandas.read_json', return_value=pd.DataFrame({
        'Restaurant Id': [1, 2],
            'Restaurant Name': ['Restaurant A', 'Restaurant B'],
            'Country': ['USA', 'Canada'],
            'City': ['New York', 'Toronto'],
            'User Rating Votes': [200, 150],  
            'User Aggregate Rating': [4.5, 4.0],
            'Cuisines': ['Mexican', 'Chinese'],
            'Event Date': ['2025-03-01', '2025-03-02']
    }))
    def test_process_successful(self, mock_read_json, mock_read_excel):
        result = process_restaurant_details()
        mock_read_json.assert_called_once_with("C:/Users/charm/Downloads/restaurant_data.json")
        mock_read_excel.assert_called_once_with("C:/Users/charm/Downloads/Country-Code.xlsx")

        expected_columns = ['Restaurant Id', 'Restaurant Name', 'Country', 'City',
                            'User Rating Votes', 'User Aggregate Rating', 'Cuisines', 'Event Date']
        self.assertEqual(list(result.columns), expected_columns)

    @patch('pandas.read_json', side_effect=pd.errors.EmptyDataError("No data"))
    def test_invalid_data_format(self, mock_read_json):
        with self.assertRaises(pd.errors.EmptyDataError):
            process_restaurant_details()

if __name__ == '__main__':
    unittest.main()
