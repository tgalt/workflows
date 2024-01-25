import pandas as pd

# Define the transactions from both groups
groupA = {
    'groupA #': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'a20', 'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28', 'a29', 'a30', 'a31', 'a32', 'a33', 'a34', 'a35', 'a36', 'a37', 'a38'],
    'groupA $': [170.67, 1053.42, 341.33, 88.28, 52.97, 353.10, 25017.14, 17596.15, 11923.01, 700.32, 1100.50, 459.03, 26088.21, 13923.91, 612.04, 164.78, 200.09, 141.24, 105.93, 623.81, 235.40, 2971.93, 1900.86, 153.01, 670.89, 1900.86, 224.06, 32496.97, 245.85, 18371.70, 247.17, 1235.85, 1847.60, 353.10, 283.37, 33132.55, 1059.30, 494.34]
}

groupB = {
    'groupB #': ['ARC002301', 'ARC002313', 'ARC002343', 'ARC002349', 'ARC002350', 'ARC002373', 'ARC002374', 'ARC002375', 'ARC002394', 'ARC002395', 'ARC002420', 'ARC002421', 'ARC002422', 'ARC002423', 'ARC002424', 'ARC002425', 'ARC002427', 'ARC002432', 'ARC002436', 'ARC002447', 'ARC002448'],
    'groupB $': [1076.4, 146.25, 482.57, 18602.48, 25234.88, 1100.5, 459.03, 700.32, 104.44, 335.45, 235.4, 729.74, 1900.86, 823.9, 330.14, 32496.96, 223.5, 18371.7, 5467.17, 2116.07, 235.4]}

# Convert the data into pandas DataFrames
df_groupA = pd.DataFrame(groupA)
df_groupB = pd.DataFrame(groupB)

# Merge the two DataFrames based on the dollar amounts
merged_df = pd.merge(df_groupA, df_groupB, left_on='groupA $', right_on='groupB $')

# Print the merged DataFrame
print(merged_df)