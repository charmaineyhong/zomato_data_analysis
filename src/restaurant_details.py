import pandas as pd
import json

def load_data():
    try:
        with open("data/restaurant_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("Error loading JSON:", e)
        raise

    if not data or "restaurants" not in data[0]:
        raise ValueError("Invalid JSON structure. Expected key 'restaurants' not found.")
    
    records = []
    for item in data[0]["restaurants"]:
        restaurant = item.get("restaurant", {})
        rec_id = restaurant.get("id", "NA")
        name = restaurant.get("name", "NA")
        country = "India"
        location = restaurant.get("location", {})
        city = location.get("city", "NA")
        user_rating = restaurant.get("user_rating", {})
        rating_votes = user_rating.get("votes", "NA")
        aggregate_rating = user_rating.get("aggregate_rating", "NA")
        cuisines = restaurant.get("cuisines", "NA")
        zomato_events = restaurant.get("zomato_events", [])
        if zomato_events and isinstance(zomato_events, list):
            event_date = zomato_events[0]["event"].get("start_date", "NA")
        else:
            event_date = "NA"
        
        record = {
            "Restaurant Id": rec_id,
            "Restaurant Name": name,
            "Country": country,
            "City": city,
            "User Rating Votes": rating_votes,
            "User Aggregate Rating": aggregate_rating,
            "Cuisines": cuisines,
            "Event Date": event_date
        }
        records.append(record)
    
    restaurants_df = pd.DataFrame(records)
    
    try:
        country_codes = pd.read_excel("data/Country-Code.xlsx")
    except Exception as e:
        print("Error loading Country-Code.xlsx:", e)
        raise

    return restaurants_df, country_codes

def process_restaurant_details():
    restaurants, country_codes = load_data()
    
    print("Restaurants DataFrame columns:", restaurants.columns.tolist())
    print("Country Codes DataFrame columns:", country_codes.columns.tolist())
    
    merged_data = pd.merge(restaurants, country_codes, on='Country', how='inner')
    processed_data = merged_data.fillna('NA')

    columns_to_save = [
        'Restaurant Id', 'Restaurant Name', 'Country', 'City',
        'User Rating Votes', 'User Aggregate Rating', 'Cuisines', 'Event Date'
    ]
    processed_data = processed_data[columns_to_save]
    
    try:
        processed_data.to_csv('outputs/restaurant_details.csv', index=False)
        print("Restaurant details processed and saved successfully.")
    except Exception as e:
        print("Error saving CSV:", e)
        raise
    
    return processed_data

if __name__ == '__main__':
    process_restaurant_details()
