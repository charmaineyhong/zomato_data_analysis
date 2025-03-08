import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from src.data_loader import load_restaurants, load_country_codes


class TestLoadRestaurants(unittest.TestCase):
    @patch('pandas.read_json')
    def test_load_restaurants_success(self, mock_read_json):
        mock_df = pd.DataFrame({
            'Restaurant Id': [1, 2],
            'Restaurant Name': ['Restaurant A', 'Restaurant B'],
            'Country': ['USA', 'Canada'],
            'City': ['New York', 'Toronto'],
            'User Rating Votes': [120, 300],
            'User Aggregate Rating': [4.5, 4.0],
            'Cuisines': ['Italian', 'French'],
            'Event Date': ['2021-05-15', '2021-05-16']
        })
        mock_read_json.return_value = mock_df

        result = load_restaurants('dummy_path.json')

        pd.testing.assert_frame_equal(result, mock_df)
        mock_read_json.assert_called_once_with('dummy_path.json')

    @patch('pandas.read_json')
    def test_load_restaurants_file_not_found(self, mock_read_json):
        mock_read_json.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            load_restaurants('nonexistent_path.json')

class TestLoadCountryCodes(unittest.TestCase):
    @patch('pandas.read_excel')
    def test_load_country_codes_success(self, mock_read_excel):
        mock_df = pd.DataFrame({'Code': ['US'], 'Country': ['United States']})
        mock_read_excel.return_value = mock_df

        result = load_country_codes('dummy_path.xlsx')

        pd.testing.assert_frame_equal(result, mock_df)
        mock_read_excel.assert_called_once_with('dummy_path.xlsx')

if __name__ == '__main__':
    unittest.main()
