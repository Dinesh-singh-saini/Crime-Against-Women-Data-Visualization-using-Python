import pandas as pd
import matplotlib.pyplot as plt

# For testing the function only
# last tested code
# visualize_data_by_crime()
# nikkama file hai testing ke liye rakh skte ho yadi man hai toh

file_path = 'NCRB women crime data (2001 - 2012).csv'
data = pd.read_csv(file_path)

states = input("Enter State/UT names to compare (comma-separated): ").split(',')
states = [state.strip() for state in states]

state_data = data[data['STATE/UT'].isin(states)].set_index('STATE/UT')

if state_data.empty:
    print("No data found for the entered states. Please check your input.")
yearly_data = state_data.iloc[:, 2:]
yearly_data_T = yearly_data.T
plt.figure(figsize=(20, 13))
yearly_data_T.plot(marker='.', ax=plt.gca())
plt.title("Crime Trends Comparison for Selected States/UTs")
plt.xticks(ticks=range(len(yearly_data_T.index)), labels=yearly_data_T.index)
plt.ylabel('Number of Crimes')
plt.xlabel('Year')
plt.grid()
plt.tight_layout()
plt.show()
