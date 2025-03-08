from src.data_loader import load_data
from src.restaurant_details import process_restaurant_details
from src.event_processor import process_events
from src.ratings_analyzer import analyze_ratings

def main():
    restaurant_data, country_codes, events_data = load_data()
    
    restaurant_details = process_restaurant_details(restaurant_data, country_codes)
    
    events = process_events(events_data)
    
    ratings_analysis = analyze_ratings(restaurant_data)

    restaurant_details.to_csv('outputs/restaurant_details.csv', index=False)
    events.to_csv('outputs/restaurant_events.csv', index=False)

if __name__ == "__main__":
    main()
