import pandas as pd
import json
# Load JSON data
with open('output_Edu.json') as f:
    data = json.load(f)

# Convert JSON to DataFrame
df = pd.json_normalize(data)

# Save DataFrame to CSV file
df.to_csv('data.csv', index=False)