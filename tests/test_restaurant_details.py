import unittest
from unittest.mock import patch, mock_open
import pandas as pd
import json
from src.restaurant_details import process_restaurant_details

class TestRestaurantDetails(unittest.TestCase):
    def setUp(self):
        self.sample_json_missing = [
            {
                "results_found": 2,
                "results_start": 1,
                "results_shown": 2,
                "restaurants": [
                    {
                        "restaurant": {
                            "id": "1",
                            "name": "Restaurant A",
                            "location": {"city": "New York"},
                            "user_rating": {"votes": 200, "aggregate_rating": "4.5"},
                            "cuisines": "Mexican",
                            "zomato_events": []  
                        }
                    },
                    {
                        "restaurant": {
                            "id": "2",
                            "name": "Restaurant B",
                            "location": {"city": "Toronto"},
                            "user_rating": {},  
                            "cuisines": "Chinese",
                            "zomato_events": []  
                        }
                    }
                ]
            }
        ]
        
        self.expected_missing = pd.DataFrame([
            {
                "Restaurant Id": "1",
                "Restaurant Name": "Restaurant A",
                "Country": "India", 
                "City": "New York",
                "User Rating Votes": 200,
                "User Aggregate Rating": "4.5",
                "Cuisines": "Mexican",
                "Event Date": "NA"
            },
            {
                "Restaurant Id": "2",
                "Restaurant Name": "Restaurant B",
                "Country": "India",
                "City": "Toronto",
                "User Rating Votes": "NA",  
                "User Aggregate Rating": "NA",  
                "Cuisines": "Chinese",
                "Event Date": "NA"
            }
        ]).reset_index(drop=True)

        self.sample_json_success = [
            {
                "results_found": 2,
                "results_start": 1,
                "results_shown": 2,
                "restaurants": [
                    {
                        "restaurant": {
                            "id": "1",
                            "name": "Restaurant A",
                            "location": {"city": "New York"},
                            "user_rating": {"votes": 200, "aggregate_rating": "4.5"},
                            "cuisines": "Mexican",
                            "zomato_events": []  
                        }
                    },
                    {
                        "restaurant": {
                            "id": "2",
                            "name": "Restaurant B",
                            "location": {"city": "Toronto"},
                            "user_rating": {"votes": 150, "aggregate_rating": "4.0"},
                            "cuisines": "Chinese",
                            "zomato_events": [
                                {"event": {"start_date": "2025-03-02"}}
                            ]
                        }
                    }
                ]
            }
        ]
        
        self.expected_success = pd.DataFrame([
            {
                "Restaurant Id": "1",
                "Restaurant Name": "Restaurant A",
                "Country": "India",
                "City": "New York",
                "User Rating Votes": 200,
                "User Aggregate Rating": "4.5",
                "Cuisines": "Mexican",
                "Event Date": "NA"
            },
            {
                "Restaurant Id": "2",
                "Restaurant Name": "Restaurant B",
                "Country": "India",
                "City": "Toronto",
                "User Rating Votes": 150,
                "User Aggregate Rating": "4.0",
                "Cuisines": "Chinese",
                "Event Date": "2025-03-02"
            }
        ]).reset_index(drop=True)
    
    MOCK_COUNTRY_CODES = pd.DataFrame({'Country': ['India'], 'Code': ['IN']})

    @patch("pandas.read_excel", return_value=MOCK_COUNTRY_CODES)
    @patch("json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_handle_missing_data(self, mock_file, mock_json_load, mock_read_excel):
        mock_json_load.return_value = self.sample_json_missing
        
        result = process_restaurant_details().reset_index(drop=True)
        
        self.assertEqual(result.loc[1, 'User Rating Votes'], "NA")
        self.assertEqual(result.loc[1, 'User Aggregate Rating'], "NA")
        
        pd.testing.assert_frame_equal(result, self.expected_missing)

    @patch("pandas.read_excel", return_value=MOCK_COUNTRY_CODES)
    @patch("json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_process_successful(self, mock_file, mock_json_load, mock_read_excel):
        mock_json_load.return_value = self.sample_json_success
        
        result = process_restaurant_details().reset_index(drop=True)
        
        expected_columns = ['Restaurant Id', 'Restaurant Name', 'Country', 'City',
                            'User Rating Votes', 'User Aggregate Rating', 'Cuisines', 'Event Date']
        self.assertListEqual(list(result.columns), expected_columns)
        
        pd.testing.assert_frame_equal(result, self.expected_success)

    @patch("builtins.open", new_callable=mock_open, read_data="dummy")
    @patch("json.load", side_effect=FileNotFoundError("File not found"))
    def test_file_not_found(self, mock_json_load, mock_file):
        with self.assertRaises(FileNotFoundError):
            process_restaurant_details()

    @patch("builtins.open", new_callable=mock_open, read_data="dummy")
    @patch("json.load", return_value=[])  
    def test_empty_json(self, mock_json_load, mock_file):
        with self.assertRaises(ValueError):
            process_restaurant_details()

if __name__ == '__main__':
    unittest.main()
