import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

file_path = 'NCRB women crime data (2001 - 2012).csv'
data = pd.read_csv(file_path)


def show_menu():
    print("==========================================")
    print("Select an option from the menu:")
    print("1. Visualize Data by State/UT")
    print("2. Visualize Data by Crime Type")
    print("3. Year-wise Crime Analysis")
    print("4. Top 5 States with Highest Crimes")
    print("5. Top 5 Safe States/UT")
    return int(input("Enter your choice: "))


# tested done 100%
# Visualize Data by State/UT
def visualize_data_by_state():
    print("1. Show total crimes for each State/UT")
    print("2. Compare crime trends across multiple states")
    print("3. Display crime type breakdown for a specific State/UT")
    choice = int(input("Select option: "))

    if choice == 1:
        state_totals = data.groupby('STATE/UT').sum(numeric_only=True).sum(axis=1).sort_values()
        state_totals = state_totals.astype(int)
        plt.figure(figsize=(12, 8))
        state_totals.plot(kind='bar', title="Total Crimes by State/UT")
        plt.ylabel('Total Crimes')
        plt.xlabel('State/UT')
        plt.tight_layout()
        plt.show()

    elif choice == 2:
        states = input("Enter State/UT names to compare (comma-separated): ").split(',')
        states = [state.strip() for state in states]
        state_data = data[data['STATE/UT'].isin(states)].set_index('STATE/UT')
        yearly_data = state_data.iloc[:, 2:]
        yearly_data_T = yearly_data.T
        plt.figure(figsize=(20, 13))
        yearly_data_T.plot(marker='.', ax=plt.gca())
        plt.title("Crime Trends Comparison")
        plt.xticks(ticks=range(len(yearly_data_T.index)), labels=yearly_data_T.index)
        plt.ylabel('Number of Crimes')
        plt.xlabel('Year')
        plt.grid()
        plt.tight_layout()
        plt.show()

    elif choice == 3:
        state = input("Enter State/UT name: ")
        state_data = data[data['STATE/UT'] == state].set_index('CRIME HEAD')
        yearly_data = state_data.iloc[:, 2:]
        yearly_data.T.plot(kind='bar', stacked=True, figsize=(10, 6), title=f"Crime Type Breakdown in {state}")
        plt.ylabel('Number of Crimes')
        plt.xlabel('Year')
        plt.tight_layout()
        plt.show()


# tested done 100%
# Visualize Data by Crime Type
def visualize_data_by_crime():
    print("1. Show trends for a specific crime type")
    print("2. Compare multiple crime types within a state")
    choice = int(input("Select option: "))

    if choice == 1:
        crime = input("Enter Crime Type: ").strip().upper()

        if crime not in data['CRIME HEAD'].str.upper().unique():
            print(f"Error: Crime Type '{crime}' not found in the dataset.")
        else:
            crime_data = data[data['CRIME HEAD'].str.upper() == crime]

            years = crime_data.columns[2:]
            crime_sums = crime_data[years].sum()
            plt.plot(years, crime_sums, marker='o')
            plt.title(f"Trend of {crime} over the Years")
            plt.xlabel("Year")
            plt.figure(figsize=(12, 8))
            plt.ylabel("Number of Crimes")
            plt.grid(True)
            plt.tight_layout()
            plt.show()


    elif choice == 2:
        state = input("Enter State/UT: ").strip().title()

        if state not in data['STATE/UT'].unique():
            print(f"Error: State/UT '{state}' not found in the dataset.")
        else:
            state_data = data[data['STATE/UT'] == state].set_index('CRIME HEAD').iloc[:,
                         2:]

            if state_data.empty:
                print(f"No data available for state: {state}")
            else:
                years = state_data.columns
                plt.figure(figsize=(12, 8))
                for crime_type in state_data.index:
                    plt.plot(years, state_data.loc[crime_type], marker='.', label=crime_type)

                plt.title(f"Comparison of Crime Types in {state}")
                plt.xlabel("Year")
                plt.ylabel("Number of Crimes")
                plt.legend(title='Crime Types')
                plt.grid(True)
                plt.tight_layout()
                plt.show()


# tested done 100%
# Year-wise Crime Analysis
def year_wise_analysis():
    print("1. Display total crimes for each year")
    print("2. Show year-over-year crime changes for a specific crime")
    choice = int(input("Select option: "))

    if choice == 1:
        year_columns = data.columns[2:]
        year_totals = data[year_columns].sum()
        plt.plot(year_columns, year_totals, marker='o')
        plt.title("Total Crimes per Year")
        plt.xlabel("Year")
        plt.ylabel("Total Crimes")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    elif choice == 2:
        crime = input("Enter Crime Type: ")
        if crime in data['CRIME HEAD'].values:
            crime_data = data[data['CRIME HEAD'] == crime].iloc[:, 2:].sum()

            plt.figure(figsize=(10, 6))
            plt.plot(crime_data.index, crime_data.values, marker='o')
            plt.title(f"Year-over-Year Change for {crime}")
            plt.xlabel("Year")
            plt.ylabel("Total Crimes")
            plt.grid(True)
            plt.tight_layout()
            plt.show()


# tested done 100%
# Top 5 States with Highest Crimes
def top_5_states_highest_crimes():
    print("1. Top 5 states with highest crimes in a specific year")
    print("2. Top 5 states with highest total crimes over all years")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        year = input("Enter year (2001 - 2012): ")
        if year in data.columns:
            top_5 = data.groupby('STATE/UT')[year].sum().sort_values(ascending=False).head(7).iloc[2:7]
            top_5.plot(kind='bar', figsize=(10, 6), title=f"Top 5 States with Highest Crimes in {year}")
            plt.ylabel('Total Crimes')
            plt.xlabel('States/UT')
            plt.tight_layout()
            plt.show()
        else:
            print(f"Year {year} not found in dataset. Please try again.")

    elif choice == '2':
        top_5 = data.groupby('STATE/UT').sum(numeric_only=True).sum(axis=1).sort_values(ascending=False).head(5)
        top_5.plot(kind='bar', figsize=(10, 6), title="Top 5 States with Highest Total Crimes (All Years)")
        plt.ylabel('Total Crimes')
        plt.xlabel('States/UT')
        plt.tight_layout()
        plt.show()

    else:
        print("Invalid choice. Please enter 1 or 2.")


#   tested done 100%
# Top 5 Safe States/UT
def top_5_safe_states():
    print("1. Top 5 safest states in a specific year")
    print("2. Top 5 safest states over all years")
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        year = input("Enter the year (2001 - 2012): ")
        if year in data.columns:
            print(f"Top 5 safest states/UTs in the year {year}")
            safe_states = data.groupby('STATE/UT')[year].sum().sort_values().head(5)
            safe_states.plot(kind='bar', title=f"Top 5 Safe States/UT in {year}")
            plt.ylabel('Total Crimes')
            plt.tight_layout()
            plt.show()
        else:
            print(f"Year {year} is not available in the dataset.")

    elif choice == 2:
        print("Top 5 safest states/UTs over all years")
        safe_states = data.groupby('STATE/UT').sum(numeric_only=True).sum(axis=1).sort_values().head(5)
        safe_states.plot(kind='bar', title="Top 5 Safe States/UT (All Years)")
        plt.ylabel('Total Crimes')
        plt.tight_layout()
        plt.show()

    else:
        print("Invalid choice. Please enter 1 or 2.")

# starts main from here

print("WOMEN CRIME DATA ANALYSIS DURING 2001-2012 IN INDIA using NCRB data || https://www.data.gov.in/resource/crime-against-women-during-2001-2012")
print('Made with ❤️ by: @Dinesh-singh-saini')
while True:
    choice = show_menu()

    if choice == 1:
        visualize_data_by_state()
    elif choice == 2:
        visualize_data_by_crime()
    elif choice == 3:
        year_wise_analysis()
    elif choice == 4:
        top_5_states_highest_crimes()
    elif choice == 5:
        top_5_safe_states()
    else:
        print("Invalid option, please try again.")
        
