# Group 3 Python Repository - Master's II Semester
![](https://www.agh.edu.pl/repozytoria/__processed__/a/2/csm_agh_znak_negatyw_bez_nazwy_1558c4077f.webp)
This repository contains the code and resources for Group 3's Python projects for the Master's II semester.

| Name     | Surname  | Funcion            |
|----------|-----------|--------------------|
| Bartosz     | Augustyn  | Project Lider |
| Tymoteusz   | Maj     | Programmer         |
| Kaushika    | Madushani|   Programmer          |
| Hubert    | Dębowski | Programmer             |
| Michał| Walencik    | Coffe Maker |

# Geographic Data Visualization and Elevation Analysis

## What is Markdown
Markdown is a simple markup language for formatting text, readable in its raw form. It uses characters like # for headings, * for italics, ** for bold. Allows you to create lists, tables, links, code. Popular in documentation and on GitHub.

[A little more information about Markdown.](https://www.markdownguide.org/extended-syntax/)

## Syntax
Markdown allows for formatting documents in a simple and readable way. For example, one can start with a main header to give the document a title, and then add a few paragraphs with bold and italicized text for emphasis. Lists can be included, links to websites can be added, and even images can be embedded. If there is a need to share code snippets, Markdown makes this clear, ensuring that they are easy to read and understand.
The combination of these features allows for the creation of well-organized, structured, and visually appealing documents that can be easily converted to HTML or other formats for use on websites, in reports, or in presentations. 

## Project Overview
This repository focuses on the visualization and statistical analysis of geographic coordinate and elevation data. The primary aim of this project is to provide insights into terrain structure by mapping spatial variations in elevation and computing key statistical metrics. The analysis includes both graphical representations of geographical coordinates and detailed descriptive statistics of elevation values. The project employs Python for data processing and visualization, using pandas, matplotlib, and seaborn libraries.

## Importance of Elevation Data in Geospatial Analysis
Elevation data plays a crucial role in various fields, including urban planning, environmental monitoring, and resource management. Understanding the spatial distribution of elevation can aid in identifying natural formations such as hills, valleys, or plateaus, as well as human impacts on the environment. By applying advanced analytical tools, we can derive meaningful conclusions regarding terrain variability, which is particularly useful in ecological, agricultural, or urbanization studies.

## Visualization of Geographic Coordinates and Elevation
The plot below illustrates the geographic coordinates (X, Y) with elevation data (Z) represented by a color gradient, offering an intuitive understanding of the terrain's structure.
![screen1](https://github.com/user-attachments/assets/175d048e-66de-49f2-a3f4-48ceff0a5a75)

### Plot 1: Geographic Coordinates and Elevation
To recreate the visualization, the following Python script is used:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# team3 - Data processing and visualization script

def load_data(file_path):
    return pd.read_csv(file_path)

def plot_coordinates_and_elevation(df):
    x = df['X']
    y = df['Y']
    z = df['Z']
    
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(x, y, c=z, cmap='viridis', s=10)
    plt.colorbar(scatter, label='Elevation (Z)')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Geographic Coordinates and Elevation')
    plt.show()

# Define the file path
file_path = r'C:\Users\Python\projekty\python_proj\data.csv'

# Load data and create the plot
df = load_data(file_path)
plot_coordinates_and_elevation(df)
```
# Detailed Analysis of Elevation (Z)
## Understanding Terrain Variations 
The above scatterplot provides a detailed representation of how the elevation varies across the geographical area. A key feature of this visualization is the color gradient, where the lighter shades (light green) represent higher elevations, and darker shades (dark blue) correspond to lower elevations. This gradient offers a visual summary of the terrain's morphology, which could indicate the presence of various geographical formations such as hills, valleys, or low-lying areas, potentially influenced by natural and man-made factors.

## Elevation (Z) Highlights:
Light green areas: Represent elevated regions, with Z values typically above 250.
Darker areas: Correspond to lower elevation regions, where Z values are typically below 230.

## Clustering and Terrain Structure
The plot also reveals clusters of points with similar characteristics, which could be analyzed further for understanding the spatial patterns of elevation. These clusters might indicate distinct zones within the terrain, with potential applications in fields such as environmental conservation, urban development, or flood risk analysis.

# Statistical Analysis of Elevation (Z)
The second phase of the project delves into the statistical analysis of elevation data, providing insights into the central tendencies, spread, and overall distribution of the Z values. The following statistics and visualizations are crucial for understanding the elevation profile of the area under investigation.

![screen2](https://github.com/user-attachments/assets/6543a519-25c6-4049-9670-9897c7e543db)


## Descriptive Statistics of Elevation (Z)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# team3 - Elevation statistics analysis

def elevation_statistics(df):
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

# Define file path and load data
file_path = r'C:\Users\Python\projekty\python_proj\data.csv'
df = pd.read_csv(file_path)

# Perform elevation statistics analysis
elevation_statistics(df)

```

## Statistical Summary:
- **Mean Elevation (Z)**: 237.48
- **Median Elevation (Z)**: 236.91
- **Minimum Elevation (Z)**: 222.14
- **Maximum Elevation (Z)**: 258.24
- **Standard Deviation (Z)**: 5.14
- **Range of Elevation (Z)**: 36.10

### Correlation Matrix

|     |     X     |     Y     |     Z     |
|-----|-----------|-----------|-----------|
|  X  |  1.000    | -0.010    | -0.030    |
|  Y  | -0.010    |  1.000    |  0.311    |
|  Z  | -0.030    |  0.311    |  1.000    |

These statistics provide a detailed overview of the terrain's elevation, showing a moderately varied landscape. The standard deviation indicates how dispersed the elevation values are from the mean, while the range highlights the difference between the highest and lowest points in the dataset.

# Conclusion
The visualizations and statistical analyses provided in this repository offer comprehensive insights into the spatial patterns of elevation within a given geographical region. The techniques demonstrated here are valuable tools in a variety of geospatial disciplines, including:

Urban Planning: Identifying suitable locations for infrastructure based on elevation and terrain variability.
Environmental Studies: Analyzing landforms for ecological and conservation purposes.
Disaster Risk Management: Using elevation data to model flood zones or areas prone to landslides.
Future work can extend this analysis to include more complex terrain metrics or integrate additional datasets, such as land cover or hydrological features, for a deeper understanding of the landscape's dynamics.
