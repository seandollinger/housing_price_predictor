import pandas as pd
 
from src.utils import read_from_file, write_to_file  # Adjusted import based on your file structure

def main():
    # Define the file name
    file_name = 'data.xlsx'

    # Read the data from the Excel file
    df = read_from_file(file_name)
    print("Data read from file:")
    print(df)

    # Modify the DataFrame as needed (example: add a new column)
    df['new_column'] = 'Sample Data'
    print("\nData after modification:")
    print(df)

    # Write the modified DataFrame back to the Excel file
    write_to_file(file_name, df)
    print(f"\nData written back to {file_name}")

if __name__ == "__main__":
    main()

