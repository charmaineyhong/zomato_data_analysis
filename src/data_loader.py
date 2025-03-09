import pandas as pd

def load_restaurants(filepath="C:/Users/charm/Downloads/restaurant_data.json"):
    """
    Load the restaurant data

    Parameters:
        filepath (str): Path to the JSON file containing restaurant data
        
    Returns:
        pd.DataFrame: DataFrame containing the restaurant data
    """
    try:
        data = pd.read_json(filepath)
        print("Restaurant data loaded successfully")
        return data
    except FileNotFoundError:
        print(f"Error: The file {filepath} not found")
        raise
    except ValueError:
        print("Error: The file not in a proper JSON format")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def load_country_codes(filepath="C:/Users/charm/Downloads/Country-Code.xlsx"):
    """
    Load the country codes

    Parameters:
        filepath (str): Path to the Excel file containing country codes
        
    Returns:
        pd.DataFrame: DataFrame containing the country codes
    """
    try:
        data = pd.read_excel(filepath)
        print("Country codes data loaded successfully")
        return data
    except FileNotFoundError:
        print(f"Error: The file {filepath} not found")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    try:
        restaurants = load_restaurants()
        country_codes = load_country_codes()
    except Exception as e:
        print(f"Failed to load data: {e}")
