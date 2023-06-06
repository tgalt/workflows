import pandas as pd
import sys

# Get the file name from the command line arguments
file_name = sys.argv[1]

# Load the data from the CSV file
df = pd.read_csv(file_name, sep='\t')

# Modify the Amount column
df['Amount'] = df.apply(lambda row: -row['Amount'] if row['CR/DR'] == 'DR' else row['Amount'], axis=1)

# Write the data back to the CSV file
df.to_csv(file_name, sep='\t', index=False)
