# Zomato Data Analysis Project

## Project Overview
This Python application was developed to assist Steven, a travel blogger, in analyzing restaurant data from Zomato for his food series project. The application processes and analyzes various aspects of restaurant data, focusing on extracting details, managing events, and analyzing ratings. The goal is to provide insightful and actionable information that can enhance the content of the travel and food series.

## Data Sources
The application uses the following data files:
- **List of Restaurants**: Contains comprehensive details about each restaurant.
- **Country Code (Excel format)**: Used to match restaurants with their respective country codes.

## Tasks and Modules
The application comprises several modules, each responsible for specific tasks:

### Restaurant Details:
- **Function**: Extracts and saves restaurant details like ID, name, country, city, user rating votes, user aggregate rating, cuisines, and event dates.
- **Output**: Data is saved to `restaurant_details.csv`.

### Events:
- **Function**: Processes and extracts events occurring in April 2019.
- **Fields Extracted**: Event ID, restaurant ID, name, photo URL, title, and event dates.
- **Output**: Data is saved to `restaurant_events.csv`.

### Ratings:
- **Function**: Analyzes the relationship between aggregate ratings and textual rating descriptions (Excellent, Very Good, Good, Average, Poor).
- **Documentation**: Documents the analysis approach and findings.
