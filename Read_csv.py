import pandas as pd

def read_excel_file(file_path):

    try:
        
        data = pd.read_excel(file_path)
        print("CSV file read successfully!")
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except pd.errors.ParserError:
        print("Error: Could not parse the CSV file.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'z_geoportal_up42 (1).csv'  

df = read_excel_file(file_path)


if df is not None:
    print(df.head())  
