import pandas as pd

def load_data():
    restaurants = pd.read_json("C:/Users/charm/Downloads/restaurant_data.json")  
    country_codes = pd.read_excel("C:/Users/charm/Downloads/Country-Code.xlsx")
    return restaurants, country_codes

def process_restaurant_details():
    restaurants, country_codes = load_data()
    merged_data = pd.merge(restaurants, country_codes, on='Country', how='inner')
    processed_data = merged_data.fillna('NA')
    columns_to_save = [
        'Restaurant Id', 'Restaurant Name', 'Country', 'City',
        'User Rating Votes', 'User Aggregate Rating', 'Cuisines', 'Event Date'
    ]
    processed_data = processed_data[columns_to_save]
    processed_data.to_csv('outputs/restaurant_details.csv', index=False)
    print("Restaurant details processed and saved successfully.")
    return processed_data

if __name__ == '__main__':
    process_restaurant_details()
