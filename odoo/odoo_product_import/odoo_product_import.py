# Description: This script is used to process the Excel file for the Odoo product import. It reads the original spreadsheet and the new spreadsheet, and fills in the quantities and locations from the original spreadsheet into the new spreadsheet. The modified spreadsheet is then saved to a new file.
# Usage: python odoo_product_import.py
# Note: Make sure the original_spreadsheet.xlsx and new_spreadsheet.xlsx files are present in the same directory as this script.
# Note: This script requires the pandas library to be installed. You can install it using pip: pip install pandas

import pandas as pd
import sys

def process_excel():
    # Load the original spreadsheet (s0) and the new spreadsheet (s1)
    try:
        s0 = pd.read_excel("original_spreadsheet.xlsx")
        s1 = pd.read_excel("new_spreadsheet.xlsx")
    except FileNotFoundError:
        print("Error: Could not find input Excel file(s). Make sure 'original_spreadsheet.xlsx' and 'new_spreadsheet.xlsx' are present.")
        sys.exit(1)

    # Create a dictionary to map SKU to Counted Quantity and Location from s0
    sku_to_qty_loc = dict(zip(s0["SKU"], zip(s0["Counted Quantity"], s0["Location"])))

    # Function to fill in quantities into s1 from s0
    def fill_quantities(row):
        sku = row["default_code"]
        if sku in sku_to_qty_loc:
            row["Quantity"] = sku_to_qty_loc[sku][0]  # Fill Quantity from s0
            row["Location"] = sku_to_qty_loc[sku][1]  # Fill Location from s0
        return row

    # Apply the function to each row in s1
    s1 = s1.apply(fill_quantities, axis=1)

    # Save the modified s1 (including original data and new data) to a new spreadsheet
    s1.to_excel("modified_spreadsheet.xlsx", index=False)

if __name__ == "__main__":
    process_excel()
