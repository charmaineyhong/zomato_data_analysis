import unittest
from unittest.mock import patch
import pandas as pd
from src.ratings_analyzer import analyze_ratings

class TestRatingsAnalyzer(unittest.TestCase):
    def setUp(self):
        self.valid_data = pd.DataFrame({
            'Restaurant Id': [1, 2, 3, 4, 5],
            'Restaurant Name': ['A', 'B', 'C', 'D', 'E'],
            'Country': ['USA', 'USA', 'USA', 'USA', 'USA'],
            'City': ['NY', 'LA', 'CHI', 'HOU', 'PHI'],
            'User Rating Votes': [100, 200, 150, 120, 130],
            'User Aggregate Rating': [3.5, 4.2, 2.8, 4.8, 3.9],
            'Cuisines': ['Italian', 'Chinese', 'Mexican', 'Thai', 'American'],
            'Event Date': ['2025-03-01']*5
        })

    @patch('pandas.DataFrame.to_csv')
    @patch('pandas.read_csv')
    def test_analyze_ratings_success(self, mock_read_csv, mock_to_csv):
        mock_read_csv.return_value = self.valid_data.copy()

        result = analyze_ratings()

        mock_read_csv.assert_called_once_with('outputs/restaurant_details.csv')
        mock_to_csv.assert_called_once_with('outputs/restaurant_ratings_analysis.csv', index=False)
        self.assertIn('Rating Text', result.columns)

        ratings = self.valid_data['User Aggregate Rating']
        q20 = ratings.quantile(0.20)
        q40 = ratings.quantile(0.40)
        q60 = ratings.quantile(0.60)
        q80 = ratings.quantile(0.80)

        def expected_category(r):
            if r <= q20:
                return 'Poor'
            elif r <= q40:
                return 'Average'
            elif r <= q60:
                return 'Good'
            elif r <= q80:
                return 'Very Good'
            else:
                return 'Excellent'

        expected_categories = ratings.apply(expected_category)
        pd.testing.assert_series_equal(
            result['Rating Text'].reset_index(drop=True),
            expected_categories.reset_index(drop=True),
            check_names=False
        )

    @patch('pandas.read_csv', side_effect=FileNotFoundError("File not found"))
    def test_file_loading_error(self, mock_read_csv):
        with self.assertRaises(FileNotFoundError):
            analyze_ratings()

    @patch('pandas.DataFrame.to_csv')
    @patch('pandas.read_csv')
    def test_missing_or_invalid_ratings(self, mock_read_csv, mock_to_csv):
    
        invalid_data = self.valid_data.copy()
        invalid_data.loc[0, 'User Aggregate Rating'] = 'invalid'
        invalid_data.loc[1, 'User Aggregate Rating'] = None

        mock_read_csv.return_value = invalid_data

        result = analyze_ratings()

        self.assertTrue(len(result) < len(invalid_data))
        self.assertTrue(pd.api.types.is_numeric_dtype(result['User Aggregate Rating']))

    @patch('pandas.read_csv', return_value=pd.DataFrame())
    def test_empty_data(self, mock_read_csv):
        with self.assertRaises(KeyError):
            analyze_ratings()

if __name__ == '__main__':
    unittest.main()
