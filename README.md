# Zomato Data Analysis Project

## Project Overview

This Python application analyzes restaurant data from Zomato. It processes and analyzes restaurant data and includes details, events, and ratings, for insights to restaurants. 

## Data Sources

The application uses the following provided data files:

- **List of Restaurants**: Contains details about each restaurant.
- **Country Code**: Shows each country's country codes.

## Modules

The application consists of several modules, each handling specific tasks:

### Data Loader (data_loader.py)
This module is responsible for loading and validating the input data. It reads restaurant data from a JSON file and country codes from an Excel file. The data loader includes error handling to catch issues such as missing files or incorrect file formats. It ensures that the raw data is correctly loaded into Pandas DataFrames, ready for further processing.

### Restaurant Details (restaurant_details.py)
This module processes the static restaurant data. It extracts key fields such as Restaurant Id, Restaurant Name, City, User Rating Votes, User Aggregate Rating, Cuisines, and Event Date. Importantly, it also extracts a country identifier from the restaurant’s location. The module then merges this information with the country codes from the Excel file to map each restaurant’s country identifier to its corresponding country name. After handling missing values (by filling with “NA”), the processed data is saved as a CSV file (restaurant_details.csv) for later use.

### Events (event_processor.py)
The event processor extracts event-specific details from the restaurant data. It iterates over each restaurant’s “zomato_events” and extracts event-related fields including Event Id, Restaurant Id, Restaurant Name, Photo URL, Event Title, Event Start Date, and Event End Date. The module converts the event date fields to datetime objects and then filters the events to include only those overlapping with April 2019. The final filtered data is exported as a CSV file (restaurant_events.csv).

### Ratings Analyzer (ratings_analyzer.py)
This module analyzes the relationship between numerical aggregate ratings and qualitative rating texts. It reads the processed restaurant details CSV, converts the “User Aggregate Rating” column to a numeric format, and computes quantiles (20th, 40th, 60th, and 80th percentiles) to establish thresholds. Based on these thresholds, each restaurant is assigned a rating text—Poor, Average, Good, Very Good, or Excellent. The analysis not only provides a distribution of these qualitative categories but also documents the approach and insights from the data. The final ratings analysis is saved to a CSV file (restaurant_ratings_analysis.csv).

Further analysis can be seen below in Usage Examples

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
- If successfully run, " Restaurant details processed and saved successfully." logging will appear in the terminal and output can be found in outputs/restaurant_details.csv

### Extract Events

```bash
python src/event_processor.py
```
- If successfully run, "Event details processed and saved successfully." logging will appear in the terminal and output can be found in outputs/restaurant_events.csv

### Analyze Ratings

```bash
python src/ratings_analyzer.py
```
- If successfully run, in the terminal, it will show the computed thresholds which is the calculated 20th, 40th, 60th, and 80th percentiles of the aggregate ratings of the restaurants.
- Based on these calculated percentiles, each restaurant is categorized into one of five textual rating categories.
- These are how each ratings are categorized
- Ratings ≤ 4.2: "Poor"
- Ratings > 4.2 and ≤ 4.4: "Average"
- Ratings > 4.4 and ≤ 4.5: "Good"
- Ratings > 4.5 and ≤ 4.6: "Very Good"
- Ratings > 4.6: "Excellent"
- A rating text of how many restaurants obtained the specific textual rating categories (Excellent, Very Good, Good, Average, Poor) are also given in the logging
- A successful logging of "Ratings analysis saved to outputs/restaurant_ratings_analysis.csv" will be shown when the module is successfully run.
  
## Testing

Unit tests are in the `tests/` directory. They cover data loading, processing, and analysis functionalities.

Run all tests using:

```bash
python -m unittest discover -s tests
```

## Key Design Decisions

- **Modular Structure**: The project uses separate modules for data loading, processing restaurant details, events extraction, and ratings analysis. This separation allows for easier maintenance, testing, and potential future expansion. 
- **Error Handling**: The code robustly handles errors such as missing files, incorrect JSON structure, and merge issues. This decision was made to ensure that the application can handle real-world data inconsistencies.
- **Missing Values**: Standardized missing value handling by replacing them with "NA" to ensure consistent data processing.
- **Mapping & Data Transformation:**: A key requirement was to map country identifiers from JSON to actual country names using an Excel file. This mapping is performed during data merging, and careful consideration was given to data types to avoid merge errors. 
- **Comprehensive Testing**: Separate testing strategy with mocks was implemented to ensure module reliability.

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

## Further Improvements

This application could be further improved to be deployed in the cloud. To do so this application could be deployed as a containerized application using Docker, which encapsulates python code handling data loading, restaurant details extraction, event processing, and ratings analysis into a consistent, reproducible environment. 

The Docker image would be built from a Dockerfile that installs dependencies from the requirements.txt file and sets the entry point to the main analysis pipeline. This container can then be deployed to AWS or any other platforms

Input data (the JSON and Excel files) can reside in a cloud object storage service separating the storage from compute and ensuring data durability. After processing, output CSV files would be uploaded back to this storage for further analysis. 


  
