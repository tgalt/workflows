import pandas as pd
from itertools import combinations

# Function to find combinations of indices where the sum is equal to the target
def find_matching_indices(values, target, max_combinations):
    for r in range(1, max_combinations + 1):
        for indices in combinations(range(len(values)), r):
            if round(sum(values[i] for i in indices), 2) == round(target, 2):  # round to handle floating point arithmetic issues
                return list(indices)
    return []  # Return an empty list if no combinations match the target

# Function to match transactions from Group B to Group A
def match_transactions(df_groupA, df_groupB, max_combinations=4):
    matches = {}

    # Sort groupB by amounts to speed up the search for matches
    df_groupB_sorted = df_groupB.sort_values('$').reset_index(drop=True)

    for idxA, rowA in df_groupA.iterrows():
        amountA = rowA['$']
        matching_indices = find_matching_indices(df_groupB_sorted['$'].tolist(), amountA, max_combinations)

        # If matches are found, store them
        if matching_indices:
            matches[rowA['#']] = df_groupB_sorted.iloc[matching_indices]['#'].tolist()
            
    return matches

# Placeholder raw data for groupA and groupB
data_groupA = {
    "#": [211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 224, 225, 226, 229, 230, 231, 232, 233, 237, 238, 239, 240, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255],
    "$": [170.67, 1053.42, 341.33, 88.28, 52.97, 353.10, 25017.14, 17596.15, 11923.01, 700.32, 1100.50, 459.03, 26088.21, 13923.91, 612.04, 164.78, 200.09, 141.24, 105.93, 623.81, 235.40, 2971.93, 1900.86, 153.01, 670.89, 1900.86, 224.06, 32496.97, 245.85, 18371.70, 247.17, 1235.85, 1847.60, 353.10, 283.37, 33132.55, 1059.30, 494.34]
}

data_groupB = {
    "#": ["ARC002301", "ARC002313", "ARC002343", "ARC002349", "ARC002350", "ARC002373", "ARC002374", "ARC002375", "ARC002394", "ARC002395", "ARC002420", "ARC002421", "ARC002422", "ARC002423", "ARC002424", "ARC002425", "ARC002427", "ARC002432", "ARC002436", "ARC002447", "ARC002448"],
    "$": [1076.4, 146.25, 482.57, 18602.48, 25234.88, 1100.5, 459.03, 700.32, 104.44, 335.45, 235.4, 729.74, 1900.86, 823.9, 330.14, 32496.96, 223.5, 18371.7, 5467.17, 2116.07, 235.4]
}

# Create dataframes
df_groupA = pd.DataFrame(data_groupA)
df_groupB = pd.DataFrame(data_groupB)

# Call the function with the dataframes
matches = match_transactions(df_groupA, df_groupB, max_combinations=4)

# Print out the matches
for groupA_ref, groupB_refs in matches.items():
    print(f"GroupA Ref: {groupA_ref} matches with GroupB Refs: {groupB_refs}")
