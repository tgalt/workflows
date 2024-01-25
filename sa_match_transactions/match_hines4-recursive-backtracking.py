import pandas as pd
from itertools import combinations

def generate_combinations(transactions, max_length):
    # Ensure that even single-element combinations are tuples
    return [combo if len(combo) > 1 else (combo[0],) for i in range(1, max_length + 1)
            for combo in combinations(range(len(transactions)), i)]

def find_matching_transactions(groupA_values, groupB_values, used_a, used_b):
    for combo_a_indices in groupA_values:
        # Check and correct the type of combo_a_indices
        if not isinstance(combo_a_indices, tuple):
            combo_a_indices = (combo_a_indices,)

        if any(idx in used_a for idx in combo_a_indices):
            continue
        sum_a = sum(groupA_values[idx] for idx in combo_a_indices)

        for combo_b_indices in groupB_values:
            # Check and correct the type of combo_b_indices
            if not isinstance(combo_b_indices, tuple):
                combo_b_indices = (combo_b_indices,)

            if any(idx in used_b for idx in combo_b_indices):
                continue
            sum_b = sum(groupB_values[idx] for idx in combo_b_indices)
            if sum_a == sum_b:
                return combo_a_indices, combo_b_indices

    return None, None

def match_transactions(df_groupA, df_groupB):
    matches = {}
    used_indices_a = set()
    used_indices_b = set()

    groupA_values = df_groupA['$'].tolist()
    groupB_values = df_groupB['$'].tolist()

    combinations_a = generate_combinations(groupA_values, 4)
    combinations_b = generate_combinations(groupB_values, 4)

    while True:
        matched_a_indices, matched_b_indices = find_matching_transactions(groupA_values, groupB_values, used_indices_a, used_indices_b)
        if matched_a_indices is None or matched_b_indices is None:
            break

        matched_a_refs = [df_groupA.iloc[idx]['#'] for idx in matched_a_indices]
        matched_b_refs = [df_groupB.iloc[idx]['#'] for idx in matched_b_indices]
        matches[tuple(matched_a_refs)] = matched_b_refs

        used_indices_a.update(matched_a_indices)
        used_indices_b.update(matched_b_indices)

    return matches

# Raw data for groupA and groupB
data_groupA = {
    "#": [211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 224, 225, 226, 229, 230, 231, 232, 233, 237, 238, 239, 240, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255],
    "$": [170.67, 1053.42, 341.33, 88.28, 52.97, 353.10, 25017.14, 17596.15, 11923.01, 700.32, 1100.50, 459.03, 26088.21, 13923.91, 612.04, 164.78, 200.09, 141.24, 105.93, 623.81, 235.40, 2971.93, 1900.86, 153.01, 670.89, 1900.86, 224.06, 32496.97, 245.85, 18371.70, 247.17, 1235.85, 1847.60, 353.10, 283.37, 33132.55, 1059.30, 494.34]
}

data_groupB = {
    "#": ["ARC002301", "ARC002313", "ARC002343", "ARC002349", "ARC002350", "ARC002373", "ARC002374", "ARC002375", "ARC002394", "ARC002395", "ARC002420", "ARC002421", "ARC002422", "ARC002423", "ARC002424", "ARC002425", "ARC002427", "ARC002432", "ARC002436", "ARC002447", "ARC002448"],
    "$": [1076.4, 146.25, 482.57, 18602.48, 25234.88, 1100.5, 459.03, 700.32, 104.44, 335.45, 235.4, 729.74, 1900.86, 823.9, 330.14, 32496.96, 223.5, 18371.7, 5467.17, 2116.07, 235.4]
}

df_groupA = pd.DataFrame(data_groupA)
df_groupB = pd.DataFrame(data_groupB)

matches = match_transactions(df_groupA, df_groupB)

# Output results
for groupA_refs, groupB_refs in matches.items():
    print(f"GroupA Refs: {groupA_refs} match with GroupB Refs: {groupB_refs}")
