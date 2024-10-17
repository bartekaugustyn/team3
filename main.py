# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# team3 - Data processing and visualization script

def load_data(file_path):
    """
    Loads CSV data from the specified file path.
    
    Parameters:
    file_path (str): Path to the CSV file
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data
    """
    return pd.read_csv(file_path)

def plot_coordinates_and_elevation(df):
    """
    Plots the geographic coordinates (X, Y) with elevation (Z) as a color gradient.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing X, Y, and Z columns for coordinates and elevation
    """
    x = df['X']
    y = df['Y']
    z = df['Z']
    
    # Create a scatter plot of coordinates with elevation as color
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(x, y, c=z, cmap='viridis', s=10)
    plt.colorbar(scatter, label='Elevation (Z)')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Geographic Coordinates and Elevation')
    plt.show()

def elevation_statistics(df):
    """
    Computes and displays basic elevation (Z) statistics and visualizes the distribution.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing a column 'Z' for elevation
    """
    z = df['Z']
    
    # Compute key statistics
    stats = {
        'Mean': z.mean(),
        'Median': z.median(),
        'Min': z.min(),
        'Max': z.max(),
        'Standard Deviation': z.std(),
        'Range': z.max() - z.min(),
        'Percentiles': z.quantile([0.25, 0.5, 0.75]).values
    }
    
    # Display computed statistics
    for stat_name, stat_value in stats.items():
        print(f"{stat_name}: {stat_value}")
    
    # Plot the distribution of elevation (Z)
    plt.figure(figsize=(10, 6))
    sns.histplot(z, bins=30, kde=True)
    plt.title('Distribution of Elevation (Z)')
    plt.xlabel('Elevation (Z)')
    plt.ylabel('Frequency')
    plt.show()

    # Compute and display correlation matrix for X, Y, and Z
    correlation_matrix = df[['X', 'Y', 'Z']].corr()
    print("Correlation Matrix:\n", correlation_matrix)

def main(file_path):
    """
    Main function to load data, visualize it, and compute elevation statistics.
    
    Parameters:
    file_path (str): Path to the CSV file
    """
    # Load data
    df = load_data(file_path)
    
    # Plot coordinates with elevation
    plot_coordinates_and_elevation(df)
    
    # Calculate and display elevation statistics
    elevation_statistics(df)

# Define the path to the data file (adjust path as needed)
file_path = r'C:\Users\tymot\OneDrive\Pulpit\Python\z_geoportal_up42.csv'

# Execute the main function
if __name__ == "__main__":
    main(file_path)
