import pandas as pd

def process_events():
    try:
        data = pd.read_json('d"C:/Users/charm/Downloads/restaurant_data.json"')
    except Exception as e:
        print("Error loading file:", e)
        raise

    events = data[data['Event Id'].notna()]

    events['Event Start Date'] = pd.to_datetime(events['Event Start Date'], errors='coerce')
    events['Event End Date'] = pd.to_datetime(events['Event End Date'], errors='coerce')

    april_start = pd.Timestamp('2019-04-01')
    april_end = pd.Timestamp('2019-04-30')

    april_events = events[(events['Event Start Date'] <= april_end) & (events['Event End Date'] >= april_start)]

    fields_to_extract = [
        'Event Id',
        'Restaurant Id',
        'Restaurant Name',
        'Photo URL',
        'Event Title',
        'Event Start Date',
        'Event End Date'
    ]
    april_events = april_events[fields_to_extract]

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
