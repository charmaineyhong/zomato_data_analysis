from src.restaurant_details import process_restaurant_details
from src.event_processor import process_events
from src.ratings_analyzer import analyze_ratings

def main():
    restaurant_details = process_restaurant_details()
    
    events = process_events()
    
    ratings_analysis = analyze_ratings()

if __name__ == "__main__":
    main()
