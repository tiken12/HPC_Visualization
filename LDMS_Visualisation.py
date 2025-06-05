import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate variability and visualize columns with significant changes
def visualize_ldms_agg(csv_file, threshold=0.01):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(csv_file)

    # Display the first few rows of the data to understand the structure
    print("Loaded data:")
    print(data.head())

    # Filter out non-numeric columns (such as 'ProducerName')
    numeric_data = data.select_dtypes(include=['number'])
    
    # Calculate the standard deviation of each numeric column (to measure variability)
    variability = numeric_data.std()

    # Print the variability for each column
    print("\nColumn Variability (Standard Deviation):")
    print(variability)

    # Plot all columns that have variability greater than the threshold
    # Assuming the first column is a timestamp or index, use it for the x-axis
    if 'timestamp' in data.columns:
        x_column = 'timestamp'
        y_column = 'timestamp'
    else:
        x_column = data.columns[0]  # Use the first column if no timestamp
        y_column = data.columns[8]  # Use the seventh column if no timestamp
    
    # Filter out columns that have low variability (below the threshold)
    columns_to_plot = [col for col in numeric_data.columns if variability[col] > threshold]

    if not columns_to_plot:
        print("No columns with significant variability above the threshold.")
        return

    # Plot the data
    plt.figure(figsize=(10, 6))

    
    # Iterate over filtered columns to plot each metric
    for column in columns_to_plot:
        plt.plot(data[x_column], data[column], label=column)
        plt.plot(data[y_column], data[column], label=column)

    # Add labels and title
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    # plt.ylabel('metrics')
    plt.title('LDMS Simple Aggregation Data (Significant Changes)')
    plt.legend(loc='upper right')
   # plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()

# Example usage: replace 'simple_agg.csv' with the path to your CSV file
csv_file = 'memeater.csv'

# Adjust the threshold value to control which columns to plot based on variability
visualize_ldms_agg(csv_file, threshold=0.01)