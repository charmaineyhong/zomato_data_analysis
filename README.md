# Zomato Data Analysis Project

## Project Overview

This Python application assists Steven, a travel blogger, in analyzing restaurant data from Zomato for his food series. It processes and analyzes various aspects of restaurant data, including details, events, and ratings, to generate insights that enhance travel and food content.

## Data Sources

The application uses the following provided data files:

- **List of Restaurants**: Contains comprehensive details about each restaurant.
- **Country Code (Excel format)**: Matches restaurants with their respective country codes.

## Tasks and Modules

The application consists of several modules, each handling specific tasks:

### Restaurant Details
- Extracts details such as Restaurant ID, Name, Country, City, User Rating Votes, User Aggregate Rating, Cuisines, and Event Date.
- Saves output to `restaurant_details.csv`.

### Events
- Processes and extracts events that occurred in April 2019.
- Extracted fields include Event ID, Restaurant ID, Restaurant Name, Photo URL, Event Title, and Event Dates.
- Saves output to `restaurant_events.csv`.

### Ratings
- Analyzes the relationship between numeric aggregate ratings and textual rating categories (Excellent, Very Good, Good, Average, Poor).
- Documents analysis approach and findings.

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

### Event

```bash
python src/event_processor.py
```

### Ratings

```bash
python src/ratings_analyzer.py
```

## Testing

Unit tests are located in the `tests/` directory. They cover data loading, processing, and analysis functionalities.

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
│   ├── restaurants.csv            # Raw restaurant details
│   └── country_codes.xlsx         # Country codes
│
├── src/
│   ├── __init__.py                # Package initializer
│   ├── main.py                    # Executes full analysis
│   ├── data_loader.py             # Loads and cleans data
│   ├── restaurant_details.py      # Processes restaurant details
│   ├── event_processor.py         # Extracts events
│   └── ratings_analyzer.py        # Analyzes ratings
│
├── tests/
│   ├── __init__.py                # Package initializer for tests
│   ├── test_data_loader.py        # Tests data loading
│   ├── test_restaurant_details.py # Tests restaurant detail extraction
│   ├── test_event_processor.py    # Tests event processing
│   └── test_ratings_analyzer.py   # Tests ratings analysis
│
├── outputs/
│   ├── restaurant_details.csv     # Processed restaurant details
│   ├── restaurant_events.csv      # Processed event details
│   └── restaurant_ratings_analysis.csv      
│
│── run.py                         # Run the program
├── .gitignore                     # Ignored files
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

## Dependencies

Dependencies are listed in the `requirements.txt` file and include:

- pandas
- openpyxl (for Excel file handling)
