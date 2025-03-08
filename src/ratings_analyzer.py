import pandas as pd

def analyze_ratings():
    try:
        data = pd.read_csv('outputs/restaurant_details.csv')
    except Exception as e:
        print("Error loading restaurant details CSV:", e)
        raise

    data['User Aggregate Rating'] = pd.to_numeric(data['User Aggregate Rating'], errors='coerce')

    data = data.dropna(subset=['User Aggregate Rating'])

    q20 = data['User Aggregate Rating'].quantile(0.20)
    q40 = data['User Aggregate Rating'].quantile(0.40)
    q60 = data['User Aggregate Rating'].quantile(0.60)
    q80 = data['User Aggregate Rating'].quantile(0.80)

    print("Computed thresholds:")
    print("20th percentile:", q20)
    print("40th percentile:", q40)
    print("60th percentile:", q60)
    print("80th percentile:", q80)

    def assign_rating_text(rating):
        if rating <= q20:
            return 'Poor'
        elif rating <= q40:
            return 'Average'
        elif rating <= q60:
            return 'Good'
        elif rating <= q80:
            return 'Very Good'
        else:
            return 'Excellent'

    data['Rating Text'] = data['User Aggregate Rating'].apply(assign_rating_text)

    print("Rating text distribution:")
    print(data['Rating Text'].value_counts())

    try:
        data.to_csv('outputs/restaurant_ratings_analysis.csv', index=False)
        print("Ratings analysis saved to outputs/restaurant_ratings_analysis.csv")
    except Exception as e:
        print("Error saving ratings analysis CSV:", e)
        raise

    return data

if __name__ == '__main__':
    analyze_ratings()
