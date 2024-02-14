import sys
import pandas as pd

def compare_excel_sheets(file1, file2, output_file):
    # Read the Excel files into pandas DataFrames
    df1 = pd.read_excel(file1, index_col=None)
    df2 = pd.read_excel(file2, index_col=None)

    # Check if shapes of DataFrames are equal
    if df1.shape != df2.shape:
        print("Shapes of the DataFrames are not equal.")
        return

    # Check if columns are equal
    if not df1.columns.equals(df2.columns):
        print("Columns of the DataFrames are not equal.")
        return

    # Check for differences in values
    comparison_result = df1.values == df2.values

    # Output comparison to a new DataFrame
    comparison_df = pd.DataFrame(comparison_result, columns=df1.columns)

    # Write comparison DataFrame to a new Excel file
    comparison_df.to_excel(output_file, index=False)
    print("Comparison result saved to", output_file)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <file1.xlsx> <file2.xlsx> <output.xlsx>")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]
    compare_excel_sheets(file1, file2, output_file)

