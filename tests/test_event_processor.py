import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from src.event_processor import process_events

class TestEventProcessor(unittest.TestCase):
    def setUp(self):
        self.sample_json = [{
            "restaurants": [
                {
                    "restaurant": {
                        "id": "1",
                        "name": "Event A",
                        "zomato_events": [
                            {
                                "event": {
                                    "event_id": 101,
                                    "title": "Title A",
                                    "start_date": "2019-03-31",
                                    "end_date": "2019-04-02",
                                    "photos": [{"photo": {"url": "url1"}}]
                                }
                            }
                        ]
                    }
                },
                {
                    "restaurant": {
                        "id": "2",
                        "name": "Event B",
                        "zomato_events": [
                            {
                                "event": {
                                    "event_id": 102,
                                    "title": "Title B",
                                    "start_date": "2019-04-15",
                                    "end_date": "2019-04-20",
                                    "photos": [{"photo": {}}]  
                                }
                            }
                        ]
                    }
                },
                {
                    "restaurant": {
                        "id": "3",
                        "name": "Event C",
                        "zomato_events": [
                            {
                                "event": {
                                    "event_id": 103,
                                    "title": "Title C",
                                    "start_date": "2019-04-30",
                                    "end_date": "2019-05-02",
                                    "photos": [{"photo": {"url": "url3"}}]
                                }
                            }
                        ]
                    }
                },
                {
                    "restaurant": {
                        "id": "4",
                        "name": "Event D",
                        "zomato_events": [
                            {
                                "event": {
                                    "event_id": 104,
                                    "title": "Title D",
                                    "start_date": "2019-05-01",
                                    "end_date": "2019-05-10",
                                    "photos": [{"photo": {"url": "url4"}}]
                                }
                            }
                        ]
                    }
                }
            ]
        }]

    @patch('pandas.DataFrame.to_csv')
    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open, read_data="dummy")
    def test_process_successful(self, mock_file, mock_json_load, mock_to_csv):
        mock_json_load.return_value = self.sample_json

        result = process_events()

        expected_ids = [101, 102, 103]
        self.assertEqual(result['Event Id'].tolist(), expected_ids)

        photo_url = result.loc[result['Event Id'] == 102, 'Photo URL'].iloc[0]
        self.assertEqual(photo_url, "NA")

        expected_fields = ['Event Id', 'Restaurant Id', 'Restaurant Name', 'Photo URL', 
                           'Event Title', 'Event Start Date', 'Event End Date']
        self.assertListEqual(list(result.columns), expected_fields)

        mock_to_csv.assert_called_once_with('outputs/restaurant_events.csv', index=False)

    @patch('builtins.open', side_effect=FileNotFoundError("File not found"))
    def test_file_not_found_error(self, mock_open):
        with self.assertRaises(FileNotFoundError):
            process_events()

    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open, read_data="dummy")
    def test_empty_data(self, mock_file, mock_json_load):
        mock_json_load.return_value = [{"restaurants": []}]
        result = process_events()
        self.assertTrue(result.empty, "Expected an empty DataFrame for empty input.")

    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open, read_data="dummy")
    def test_invalid_date_format(self, mock_file, mock_json_load):
        invalid_json = [{
            "restaurants": [
                {
                    "restaurant": {
                        "id": "10",
                        "name": "Invalid Date Event",
                        "zomato_events": [
                            {
                                "event": {
                                    "event_id": 201,
                                    "title": "Invalid Event",
                                    "start_date": "not_a_date",
                                    "end_date": "not_a_date",
                                    "photos": [{"photo": {"url": "url_invalid"}}]
                                }
                            }
                        ]
                    }
                }
            ]
        }]
        mock_json_load.return_value = invalid_json
        
        result = process_events()
        self.assertTrue(result.empty, "Expected an empty DataFrame due to invalid date formats.")

if __name__ == '__main__':
    unittest.main()
