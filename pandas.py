import pandas as pd

# Read data from Excel files into DataFrames
df1 = pd.read_excel('df1.xlsx')
df2 = pd.read_excel('df2.xlsx')

# Initialize empty DataFrames for proper mapping and mixed matching
proper_mapping = pd.DataFrame(columns=['trigger', 'flow', 'business'])
mixed_matching = pd.DataFrame(columns=['trigger', 'flow', 'business'])

# Iterate through df2 rows
for index, row in df2.iterrows():
    name = row['name']
    business_group = row['business_group']

    # Check if name matches 'trigger' in df1
    trigger_match = df1[df1['trigger'] == name]

    # Check if name matches 'flow' in df1
    flow_match = df1[df1['flow'] == name]

    # If there is a match in both 'trigger' and 'flow', it's a mixed match
    if not trigger_match.empty and not flow_match.empty:
        mixed_matching = mixed_matching.append({'trigger': name, 'flow': name, 'business': business_group}, ignore_index=True)
    elif not trigger_match.empty:
        proper_mapping = proper_mapping.append({'trigger': name, 'flow': trigger_match['flow'].values[0], 'business': business_group}, ignore_index=True)
    elif not flow_match.empty:
        proper_mapping = proper_mapping.append({'trigger': name, 'flow': name, 'business': business_group}, ignore_index=True)

print("Proper Mapped result:")
print(proper_mapping)

print("\nMixed matching:")
print(mixed_matching)
