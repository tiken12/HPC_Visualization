import pandas as pd
import matplotlib.pyplot as plt

# Function to plot time vs memfree from two CSV files
def plot_time_vs_memfree(csv_file_1, csv_file_2):
    # Load the first CSV file into a DataFrame
    data1 = pd.read_csv(csv_file_1)
    
    # Load the second CSV file into a DataFrame
    data2 = pd.read_csv(csv_file_2)

    # Ensure the 'time' and 'memfree' columns exist in both datasets
    if 'time' not in data1.columns or 'memfree' not in data1.columns:
        print(f"Error: 'time' or 'memfree' column not found in {csv_file_1}.")
        return
    
    if 'time' not in data2.columns or 'memfree' not in data2.columns:
        print(f"Error: 'time' or 'memfree' column not found in {csv_file_2}.")
        return
    
    # Convert 'time' columns to datetime if necessary
    data1['time'] = pd.to_datetime(data1['time'], errors='coerce')
    data2['time'] = pd.to_datetime(data2['time'], errors='coerce')

    # Plot time vs memfree for both CSV files
    plt.figure(figsize=(10, 6))
    
    # Plot for the first CSV file
    plt.plot(data1['time'], data1['memfree'], label=f'memfree from {csv_file_1}', color='blue')
    
    # Plot for the second CSV file
    plt.plot(data2['time'], data2['memfree'], label=f'memfree from {csv_file_2}', color='red')

    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Memfree')
    plt.title('Time vs Memfree Comparison')
    plt.xticks(rotation=45)
    plt.legend(loc='upper right')
    plt.tight_layout()

    # Show the plot
    plt.show()

# Example usage: replace 'csv_file_1.csv' and 'csv_file_2.csv' with the paths to your CSV files
csv_file_1 = 'meminfo.csv'
csv_file_2 = 'memeater.csv'
plot_time_vs_memfree(csv_file_1, csv_file_2)