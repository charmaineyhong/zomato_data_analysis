# Zomato Data Analysis Project

## Project Overview

This Python application assists Steven, a travel blogger, in analyzing restaurant data from Zomato for his food series. It processes and analyzes restaurant data, including details, events, and ratings, to generate insights that enhance travel and food content.

## Data Sources

The application uses the following provided data files:

- **List of Restaurants**: Contains details about each restaurant.
- **Country Code**: Shows each country's country codes.

## Tasks and Modules

The application consists of several modules, each handling specific tasks:

### Restaurant Details
- Extracts details such as Restaurant ID, Name, Country, City, User Rating Votes, User Aggregate Rating, Cuisines, and Event Date.
- Saves output to `restaurant_details.csv`.

### Events
- Processes and extracts events that occurred in April 2019.
- Extracted fields are Event ID, Restaurant ID, Restaurant Name, Photo URL, Event Title, and Event Dates.
- Saves output to `restaurant_events.csv`.

### Ratings
- Analyzes the numeric aggregate ratings.
- Output is to give a textual rating categories (Excellent, Very Good, Good, Average, Poor) to each of the restaurants based on the numeric aggregate ratings.
- Documents analysis approach and findings in `restaurant_ratings_analysis.csv`.

## Setup Instructions

Follow these steps to run the application locally:

### 1. Clone the Repository

```bash
git clone https://github.com/charmaineyhong/zomato_data_analysis.git
```

### 2. Navigate to the Project Directory

```bash
cd zomato_data_analysis
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python run.py
```

## Usage Examples

To individually execute modules:

### Process Restaurant Data

```bash
python src/restaurant_details.py
```

### Extract Events

```bash
python src/event_processor.py
```

### Analyze Ratings

```bash
python src/ratings_analyzer.py
```

## Testing

Unit tests are in the `tests/` directory. They cover data loading, processing, and analysis functionalities.

Run all tests using:

```bash
python -m unittest discover -s tests
```

## Key Design Decisions

- **Modular Structure**: The project uses separate modules for different functionalities, improving maintainability and readability.
- **Error Handling**: Implemented try-except blocks to manage exceptions clearly and gracefully.
- **Missing Values**: Standardized missing value handling by replacing them with "NA" to ensure consistent data processing.
- **Focused Field Extraction**: Extracted only necessary fields to simplify data management and enhance clarity.
- **Comprehensive Testing**: Employed a separate testing strategy with mocks to ensure module reliability.

## Assumptions Made

- **File Path Consistency**: All modules expect data files and outputs to exist in predefined paths (e.g., `data/restaurant_data.json`, `outputs/restaurant_events.csv`).
- **Missing Data Strategy**: Filling missing values with "NA" is assumed acceptable for the project’s analytical requirements.

## System Architecture

```
zomato_data_analysis/
│
├── data/
│   ├── restaurants.csv            
│   └── country_codes.xlsx         
│
├── src/
│   ├── __init__.py               
│   ├── main.py                    
│   ├── data_loader.py             
│   ├── restaurant_details.py      
│   ├── event_processor.py         
│   └── ratings_analyzer.py        
│
├── tests/
│   ├── __init__.py                
│   ├── test_data_loader.py        
│   ├── test_restaurant_details.py 
│   ├── test_event_processor.py    
│   └── test_ratings_analyzer.py   
│
├── outputs/
│   ├── restaurant_details.csv     
│   ├── restaurant_events.csv      
│   └── restaurant_ratings_analysis.csv      
│
├── run.py                         
├── .gitignore                     
├── README.md                      
└── requirements.txt               
```

## Dependencies

Dependencies are listed in the `requirements.txt` file and include:

- pandas
- openpyxl (for Excel file handling)
