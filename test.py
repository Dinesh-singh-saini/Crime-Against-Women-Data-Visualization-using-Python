import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the data
file_path = 'NCRB women crime data (2001 - 2012).csv'
data = pd.read_csv(file_path)


# Create the main application window
class CrimeDataApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Women Crime Data Analysis")
        self.geometry("600x400")

        # Create a menu
        self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)

        analyze_menu = tk.Menu(menu)
        menu.add_cascade(label="Analyze", menu=analyze_menu)

        analyze_menu.add_command(label="Visualize Data by State/UT", command=self.visualize_data_by_state)
        analyze_menu.add_command(label="Visualize Data by Crime Type", command=self.visualize_data_by_crime)
        analyze_menu.add_command(label="Year-wise Crime Analysis", command=self.year_wise_analysis)
        analyze_menu.add_command(label="Top 5 States with Highest Crimes", command=self.top_5_states_highest_crimes)
        analyze_menu.add_command(label="Top 5 Safe States/UT", command=self.top_5_safe_states)

    def show_plot(self, fig):
        plt.close('all')
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def visualize_data_by_state(self):
        def plot_total_crimes():
            state_totals = data.groupby('STATE/UT').sum(numeric_only=True).sum(axis=1).sort_values()
            state_totals = state_totals.astype(int)
            fig, ax = plt.subplots(figsize=(12, 8))
            state_totals.plot(kind='bar', title="Total Crimes by State/UT", ax=ax)
            ax.set_ylabel('Total Crimes')
            ax.set_xlabel('State/UT')
            self.show_plot(fig)

        def plot_trends():
            states = state_entry.get().split(',')
            states = [state.strip() for state in states]
            state_data = data[data['STATE/UT'].isin(states)].set_index('STATE/UT')
            yearly_data = state_data.iloc[:, 2:]
            yearly_data_T = yearly_data.T
            fig, ax = plt.subplots(figsize=(20, 13))
            yearly_data_T.plot(marker='.', ax=ax)
            ax.set_title("Crime Trends Comparison")
            ax.set_ylabel('Number of Crimes')
            ax.set_xlabel('Year')
            self.show_plot(fig)

        def plot_breakdown():
            state = state_entry.get()
            state_data = data[data['STATE/UT'] == state].set_index('CRIME HEAD')
            yearly_data = state_data.iloc[:, 2:]
            fig, ax = plt.subplots(figsize=(10, 6))
            yearly_data.T.plot(kind='bar', stacked=True, ax=ax, title=f"Crime Type Breakdown in {state}")
            ax.set_ylabel('Number of Crimes')
            ax.set_xlabel('Year')
            self.show_plot(fig)

        # Create a new window for state/UT visualization
        window = tk.Toplevel(self)
        window.title("Visualize Data by State/UT")

        tk.Label(window, text="Enter State/UT names (comma-separated):").pack()
        state_entry = tk.Entry(window, width=50)
        state_entry.pack()

        tk.Button(window, text="Show Total Crimes", command=plot_total_crimes).pack()
        tk.Button(window, text="Compare Crime Trends", command=plot_trends).pack()
        tk.Button(window, text="Display Crime Type Breakdown", command=plot_breakdown).pack()

    def visualize_data_by_crime(self):
        def plot_trends():
            crime = crime_entry.get().strip().upper()
            if crime not in data['CRIME HEAD'].str.upper().unique():
                messagebox.showerror("Error", f"Crime Type '{crime}' not found in the dataset.")
            else:
                crime_data = data[data['CRIME HEAD'].str.upper() == crime]
                years = crime_data.columns[2:]
                crime_sums = crime_data[years].sum()
                fig, ax = plt.subplots(figsize=(12, 8))
                ax.plot(years, crime_sums, marker='o', color='red')
                ax.set_title(f"Trend of {crime} over the Years")
                ax.set_xlabel("Year")
                ax.set_ylabel("Number of Crimes")
                self.show_plot(fig)

        def plot_comparison(state_entry=None):
            state = state_entry.get().strip().title()
            if state not in data['STATE/UT'].unique():
                messagebox.showerror("Error", f"State/UT '{state}' not found in the dataset.")
            else:
                state_data = data[data['STATE/UT'] == state].set_index('CRIME HEAD').iloc[:, 2:]
                if state_data.empty:
                    messagebox.showinfo("Info", f"No data available for state: {state}")
                else:
                    years = state_data.columns
                    fig, ax = plt.subplots(figsize=(12, 8))
                    for crime_type in state_data.index:
                        ax.plot(years, state_data.loc[crime_type], marker='.', label=crime_type)
                    ax.set_title(f"Comparison of Crime Types in {state}")
                    ax.set_xlabel("Year")
                    ax.set_ylabel("Number of Crimes")
                    ax.legend(title='Crime Types')
                    self.show_plot(fig)

        # Create a new window for crime type visualization
        window = tk.Toplevel(self)
        window.title("Visualize Data by Crime Type")

        tk.Label(window, text="Enter Crime Type:").pack()
        crime_entry = tk.Entry(window, width=50)
        crime_entry.pack()

        tk.Button(window, text="Show Trends", command=plot_trends).pack()
        tk.Button(window, text="Compare Crime Types", command=plot_comparison).pack()

    def year_wise_analysis(self):
        def plot_total_crimes():
            year_columns = data.columns[2:]
            year_totals = data[year_columns].sum()
            fig, ax = plt.subplots(figsize=(12, 8))
            ax.plot(year_columns, year_totals, marker='o')
            ax.set_title("Total Crimes per Year")
            ax.set_xlabel("Year")
            ax.set_ylabel("Total Crimes")
            self.show_plot(fig)

        def plot_yearly_change():
            crime = crime_entry.get().strip()
            if crime in data['CRIME HEAD'].values:
                crime_data = data[data['CRIME HEAD'] == crime].iloc[:, 2:].sum()
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(crime_data.index, crime_data.values, marker='o')
                ax.set_title(f"Year-over-Year Change for {crime}")
                ax.set_xlabel("Year")
                ax.set_ylabel("Total Crimes")
                self.show_plot(fig)

        # Create a new window for year-wise analysis
        window = tk.Toplevel(self)
        window.title("Year-wise Crime Analysis")

        tk.Label(window, text="Enter Crime Type (if applicable):").pack()
        crime_entry = tk.Entry(window, width=50)
        crime_entry.pack()

        tk.Button(window, text="Display Total Crimes per Year", command=plot_total_crimes).pack()
        tk.Button(window, text="Show Year-over-Year Change", command=plot_yearly_change).pack()

    def top_5_states_highest_crimes(self):
        def plot_highest_crimes():
            year = year_entry.get().strip()
            if year in data.columns:
                top_5 = data.groupby('STATE/UT')[year].sum().sort_values(ascending=False).head(5)
                fig, ax = plt.subplots(figsize=(10, 6))
                top_5.plot(kind='bar', ax=ax, title=f"Top 5 States with Highest Crimes in {year}",
                           color=['#8B0000', '#A52A2A', '#B22222', '#CD5C5C', '#FF6666'])
                ax.set_ylabel('Total Crimes')
                ax.set_xlabel('States/UT')
                self.show_plot(fig)
            else:
                messagebox.showerror("Error", f"Year {year} not found in dataset. Please try again.")

        def plot_total_highest_crimes():
            data_numeric = data.copy()
            for col in data.columns:
                if col != 'STATE/UT':
                    data_numeric[col] = pd.to_numeric(data_numeric[col], errors='coerce')
            total_crimes = data_numeric.drop(columns='STATE/UT').sum(axis=1)
            state_totals = data[['STATE/UT']].copy()
            state_totals['Total Crimes'] = total_crimes
            top_5 = state_totals.groupby('STATE/UT')['Total Crimes'].sum().sort_values(ascending=False).head(5)
            fig, ax = plt.subplots(figsize=(10, 6))
            top_5.plot(kind='bar', ax=ax, title="Top 5 States with Highest Total Crimes (All Years)",
                       color=['#8B0000', '#A52A2A', '#B22222', '#CD5C5C', '#FF6666'])
            ax.set_ylabel('Total Crimes')
            ax.set_xlabel('States/UT')
            self.show_plot(fig)

        # Create a new window for top 5 states with the highest crimes
        window = tk.Toplevel(self)
        window.title("Top 5 States with Highest Crimes")

        tk.Label(window, text="Enter Year (2001 - 2012):").pack()
        year_entry = tk.Entry(window, width=50)
        year_entry.pack()

        tk.Button(window, text="Top 5 States in Year", command=plot_highest_crimes).pack()
        tk.Button(window, text="Top 5 States Overall", command=plot_total_highest_crimes).pack()

    def top_5_safe_states(self):
        def plot_safe_states():
            year = year_entry.get().strip()
            if year in data.columns:
                safe_states = data.groupby('STATE/UT')[year].sum().sort_values().head(5)
                fig, ax = plt.subplots(figsize=(10, 6))
                safe_states.plot(kind='bar', ax=ax, title=f"Top 5 Safe States/UT in {year}",
                                 color=['#006400', '#228B22', '#32CD32', '#66FF66', '#99FF99'])
                ax.set_ylabel('Total Crimes')
                self.show_plot(fig)
            else:
                messagebox.showerror("Error", f"Year {year} is not available in the dataset.")

        def plot_safe_states_all_years():
            safe_states = data.groupby('STATE/UT').sum(numeric_only=True).sum(axis=1).sort_values().head(5)
            fig, ax = plt.subplots(figsize=(10, 6))
            safe_states.plot(kind='bar', ax=ax, title="Top 5 Safe States/UT (All Years)",
                             color=['#006400', '#228B22', '#32CD32', '#66FF66', '#99FF99'])
            ax.set_ylabel('Total Crimes')
            self.show_plot(fig)

        # Create a new window for top 5 safe states
        window = tk.Toplevel(self)
        window.title("Top 5 Safe States/UT")

        tk.Label(window, text="Enter Year (2001 - 2012):").pack()
        year_entry = tk.Entry(window, width=50)
        year_entry.pack()

        tk.Button(window, text="Top 5 Safe States in Year", command=plot_safe_states).pack()
        tk.Button(window, text="Top 5 Safe States Overall", command=plot_safe_states_all_years).pack()


# Create and run the application
app = CrimeDataApp()
app.mainloop()
