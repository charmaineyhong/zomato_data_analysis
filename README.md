# Zomato Data Analysis Project

## Project Overview

This Python application analyzes restaurant data from Zomato. It processes and analyzes restaurant data and includes details, events, and ratings, for insights to restaurants. 

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
- Documents findings in `restaurant_ratings_analysis.csv`.
- Analysis approach can be seen in usage examples section

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
Ratings ≤ 4.2: "Poor"
Ratings > 4.2 and ≤ 4.4: "Average"
Ratings > 4.4 and ≤ 4.5: "Good"
Ratings > 4.5 and ≤ 4.6: "Very Good"
Ratings > 4.6: "Excellent"
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


  
