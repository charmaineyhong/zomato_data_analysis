import unittest
from unittest.mock import patch
import pandas as pd
from src.event_processor import process_events

class TestEventProcessor(unittest.TestCase):
    def setUp(self):
        self.sample_events = pd.DataFrame({
            'Event Id': [101, 102, 103, 104],
            'Restaurant Id': [1, 2, 3, 4],
            'Restaurant Name': ['Event A', 'Event B', 'Event C', 'Event D'],
            'Photo URL': ['url1', None, 'url3', 'url4'], 
            'Event Title': ['Title A', 'Title B', 'Title C', 'Title D'],
            'Event Start Date': ['2019-03-31', '2019-04-15', '2019-04-30', '2019-05-01'],
            'Event End Date': ['2019-04-02', '2019-04-20', '2019-05-02', '2019-05-10']
        })

    @patch('pandas.DataFrame.to_csv')
    @patch('pandas.read_json')
    def test_process_successful(self, mock_read_json, mock_to_csv):
        mock_read_json.return_value = self.sample_events
        result = process_events()

        expected_ids = [101, 102, 103]
        self.assertEqual(result['Event Id'].tolist(), expected_ids)

        photo_url = result.loc[result['Event Id'] == 102, 'Photo URL'].iloc[0]
        self.assertEqual(photo_url, "NA")

        expected_fields = ['Event Id', 'Restaurant Id', 'Restaurant Name', 'Photo URL', 
                           'Event Title', 'Event Start Date', 'Event End Date']
        self.assertListEqual(list(result.columns), expected_fields)

        mock_to_csv.assert_called_once_with('outputs/restaurant_events.csv', index=False)

    @patch('pandas.read_json', side_effect=FileNotFoundError("File not found"))
    def test_file_not_found_error(self, mock_read_json):
        with self.assertRaises(FileNotFoundError):
            process_events()

    @patch('pandas.read_json', return_value=pd.DataFrame())
    def test_empty_data(self, mock_read_json):
        with self.assertRaises(KeyError):
            process_events()

    @patch('pandas.read_json')
    def test_invalid_date_format(self, mock_read_json):
        invalid_date_data = pd.DataFrame({
            'Event Id': [201],
            'Restaurant Id': [10],
            'Restaurant Name': ['Invalid Date Event'],
            'Photo URL': ['url_invalid'],
            'Event Title': ['Invalid Event'],
            'Event Start Date': ['not_a_date'],
            'Event End Date': ['not_a_date']
        })
        mock_read_json.return_value = invalid_date_data
        
        result = process_events()
        self.assertTrue(result.empty, "Expected an empty DataFrame due to invalid date formats.")

if __name__ == '__main__':
    unittest.main()
