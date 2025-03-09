import pandas as pd
import json

def process_events():
    try:
        with open("C:/Users/charm/Downloads/restaurant_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("Error loading JSON file:", e)
        raise

    if not data or "restaurants" not in data[0]:
        raise ValueError("Invalid JSON structure. Expected key 'restaurants' not found.")
    
    events_list = []
    for item in data[0]["restaurants"]:
        restaurant = item.get("restaurant", {})
        restaurant_id = restaurant.get("id", "NA")
        restaurant_name = restaurant.get("name", "NA")
        zomato_events = restaurant.get("zomato_events", [])
        
        if zomato_events and isinstance(zomato_events, list):
            for event_item in zomato_events:
                event_data = event_item.get("event", {})
                event_id = event_data.get("event_id", "NA")
                event_title = event_data.get("title", "NA")
                event_start = event_data.get("start_date", "NA")
                event_end = event_data.get("end_date", "NA")
                
                photo_url = "NA"
                photos = event_data.get("photos", [])
                if photos and isinstance(photos, list):
                    first_photo = photos[0].get("photo", {})
                    photo_url = first_photo.get("url", "NA")
                
                events_list.append({
                    "Event Id": event_id,
                    "Restaurant Id": restaurant_id,
                    "Restaurant Name": restaurant_name,
                    "Photo URL": photo_url,
                    "Event Title": event_title,
                    "Event Start Date": event_start,
                    "Event End Date": event_end
                })

    if not events_list:
        print("No events found in the data.")
        return pd.DataFrame()
    
    events_df = pd.DataFrame(events_list)

    events_df['Event Start Date'] = pd.to_datetime(events_df['Event Start Date'], errors='coerce')
    events_df['Event End Date'] = pd.to_datetime(events_df['Event End Date'], errors='coerce')

    april_start = pd.Timestamp('2019-04-01')
    april_end = pd.Timestamp('2019-04-30')

    april_events = events_df[
        (events_df["Event Start Date"] <= april_end) &
        (events_df["Event End Date"] >= april_start)
    ]

    april_events = april_events.fillna("NA")

    try:
        april_events.to_csv('outputs/restaurant_events.csv', index=False)
        print("Event details processed and saved successfully.")
    except Exception as e:
        print("Error saving 'outputs/restaurant_events.csv':", e)
        raise

    return april_events

if __name__ == '__main__':
    process_events()
