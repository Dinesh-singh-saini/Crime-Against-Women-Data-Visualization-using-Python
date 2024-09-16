import pandas as pd
import matplotlib.pyplot as plt

# For testing the function only
# last tested code 
# visualize_data_by_crime()
# nikkama file hai testing ke liye rakh skte ho yadi man hai toh

file_path = 'NCRB women crime data (2001 - 2012).csv'
data = pd.read_csv(file_path)

crime = input("Enter Crime Type: ").strip().upper()
if crime not in data['CRIME HEAD'].str.upper().unique():
    print(f"Error: Crime Type '{crime}' not found in the dataset.")
else:
    crime_data = data[data['CRIME HEAD'].str.upper() == crime]
    years = crime_data.columns[2:]
    crime_sums = crime_data[years].sum()
    plt.figure(figsize=(12, 8))
    plt.plot(years, crime_sums, marker='o', color='red')
    plt.title(f"Trend of {crime} over the Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Crimes")
    plt.grid()
    plt.tight_layout()
    plt.show()
