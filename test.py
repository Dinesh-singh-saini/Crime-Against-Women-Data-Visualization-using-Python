import pandas as pd
import matplotlib.pyplot as plt

# for testing the function only
# nikkama file hai testing ke liye rakh skte ho yadi man hai toh

file_path = 'NCRB women crime data (2001 - 2012).csv'
data = pd.read_csv(file_path)

print("1. Top 5 safest states in a specific year")
print("2. Top 5 safest states over all years")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    year = input("Enter the year: ")
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
