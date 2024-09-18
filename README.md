# Crime Against Women Data Visualization using Python

## Overview

This project provides an interactive analysis and visualization of crime data against women in India from 2001 to 2012. Utilizing Python, Pandas, and Matplotlib, the tool allows users to explore trends, compare states, and analyze crime types to better understand crime patterns.

## Features

- **Visualize Data by State/UT**: 
  - Show total crimes for each State/UT. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_1.png)
  - Compare crime trends across multiple states. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_2.png)
  - Display crime type breakdown for a specific State/UT. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_3.png)
  
- **Visualize Data by Crime Type**:
  - Show trends for a specific crime type. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_4.png)
  - Compare multiple crime types within a state. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_5.png)

- **Year-wise Crime Analysis**:
  - Display total crimes for each year. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_6.png)
  - Show year-over-year crime changes for a specific crime. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_7.png)

- **Top 5 States with Highest Crimes**:
  - Identify the top 5 states with the highest crimes in a specific year. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_8.png)
  - Find the top 5 states with the highest total crimes over all years. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_9.png)

- **Top 5 Safe States/UT**:
  - Identify the top 5 safest states/UTs in a specific year. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_10.png)
  - Find the top 5 safest states/UTs over all years. ex [result](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Examples%20Results/Figure_11.png)

## Getting Started

### Prerequisites

Ensure you have the following libraries installed:
- `pandas`
- `matplotlib`

You can install these libraries using pip:
```bash
pip install pandas matplotlib
```
## Dataset

The dataset used in this project is "Crime Against Women Data" available from [Data.gov.in](https://www.data.gov.in/resource/crime-against-women-during-2001-2012). Ensure the dataset is in CSV format and located at the specified file path.

## File Structure
```
Crime-Against-Women-Data-Visualization-using-Python/
│
├── main.py                                     # Main script to run the data analysis
├── NCRB women crime data (2001 - 2012).csv     # Dataset (place it in the same directory or update the path in the script)
├── README.md                                   # This file
├── LICENSE                                     # To ensure no one can copy the project (except for educational purposes).
├── Project structure.png                       # For a better understanding of the project structure and menus.
├── Examples Results                            # This folder contains the visualization of the tested results.
├── example.JPEG                                # Collage pic of examples.
└── test.py                                     # For testing purposes.
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python.git
```
2. Navigate to the project directory:
```bash
cd Crime-Against-Women-Data-Visualization-using-Python
```
3. Run the script:
```bash
python main.py
```
4. Follow the on-screen menu to perform various analyses.

## Example

![project structure](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/Project%20structure.png)
![example](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/blob/main/example.JPG)

### Visualizing Data by State/UT

To show the total crimes for each State/UT, select option 1 under the "Visualize Data by State/UT" menu. The script will generate a bar chart displaying the total crimes for each state.

### Year-wise Crime Analysis
Select option 1 under the "Year-wise Crime Analysis" menu to display the total crimes for each year. The script will generate a line plot showing the trend of total crimes over the years.

## Example Results
You can view the results of the analyses in the [Examples Results](https://github.com/Dinesh-singh-saini/Crime-Against-Women-Data-Visualization-using-Python/tree/main/Examples%20Results) folder. This folder contains tested results and visualizations generated by the scrip

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please contact:

## Author: Dinesh Kumar
  * Email: dineshkumar623092@gmail.com
    
## Acknowledgments
  * Data source: Data.gov.in
  * Libraries used: Pandas, Matplotlib

# Made with ❤️ by Dinesh Kumar
