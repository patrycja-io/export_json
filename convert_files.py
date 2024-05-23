import os
import json
import pandas as pd

# Path to the directory containing the files
directory_path = '/Users/patrycja.tyra/Downloads/2024/May'

# List to store file names
file_names = []

# Iterate over all files in the directory
for filename in os.listdir(directory_path):
    # Append the filename to the list
    file_names.append(filename)

# Create a dictionary to store the filenames
data = {"file_names": file_names}

# Path to the output JSON file
output_json = os.path.join(directory_path, 'file_names.json')

# Write the filenames to the JSON file
with open(output_json, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f'JSON file created at: {output_json}')

# Read the JSON file into a DataFrame
df = pd.read_json(output_json)

# Path to the output CSV file
output_csv = os.path.join(directory_path, 'file_names.csv')

# Write the DataFrame to a CSV file
df.to_csv(output_csv, index=False)

print(f'CSV file created at: {output_csv}')
