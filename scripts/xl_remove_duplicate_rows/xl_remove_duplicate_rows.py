# this script removes duplicate rows from an Excel file and saves the result to a new file
# install pandas with pip install pandas
# install openpyxl with pip install openpyxl
# run the script with python remove_duplicate_rows.py
# install pyinstaller to create an executable with pip install pyinstaller

import pandas as pd

def remove_duplicate_rows(input_file, output_file):
    # Read Excel file into pandas DataFrame
    df = pd.read_excel(input_file)
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Write DataFrame to Excel file
    df.to_excel(output_file, index=False)
    
    print("Duplicate rows removed successfully and saved to", output_file)

def main():
    input_file = input("Enter the path to the input Excel file: ")
    output_file = input("Enter the path for the output Excel file: ")
    
    remove_duplicate_rows(input_file, output_file)

if __name__ == "__main__":
    main()
