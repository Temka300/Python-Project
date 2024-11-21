import pandas as pd

data = pd.read_excel('C:\\Users\\Temka\\Downloads\\koreangrammar.xlsx')
# Convert the data from the Excel file to JSON format
json_data = data.to_dict(orient='records')

# Save the JSON data to a file
json_file_path = 'C:\\Users\\Temka\\Downloads\\koreanbocab.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    import json
    json.dump({"words": json_data}, json_file, ensure_ascii=False, indent=4)

json_file_path
