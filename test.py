import pandas as pd
import matplotlib.pyplot as plt

# For testing the function only
# last tested code
# nikkama file hai testing ke liye rakh skte ho yadi man hai toh

file_path = 'NCRB women crime data (2001 - 2012).csv'
data = pd.read_csv(file_path)

states = input("Enter State/UT names to compare (comma-separated): ").split(',')
states = [state.strip() for state in states]

# Ensure 'STATE/UT' exists in your DataFrame and filter the data accordingly
if 'STATE/UT' not in data.columns:
    raise ValueError("Column 'STATE/UT' does not exist in the data.")

# Filter data based on user input and ensure 'STATE/UT' is in index
state_data = data[data['STATE/UT'].isin(states)]
if state_data.empty:
    raise ValueError("No data available for the selected states.")

# Set 'STATE/UT' as index and select columns for yearly data
state_data = state_data.set_index('STATE/UT')
yearly_data = state_data.iloc[:, 2:]  # Adjust based on your data's structure

# Transpose yearly data for plotting
yearly_data_T = yearly_data.T

# Plotting
plt.figure(figsize=(20, 13))
for state in states:
    if state in yearly_data.index:
        plt.plot(yearly_data_T.index, yearly_data_T[state], marker='.', label=state)

plt.title("Crime Trends Comparison")
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='States/UT')
plt.tight_layout()
plt.show()