import os
import json

def convert_ndjson_to_json(ndjson_dir, json_dir):
    os.makedirs(json_dir, exist_ok=True)

    for filename in os.listdir(ndjson_dir):
        if filename.endswith('.ndjson'):
            ndjson_file = os.path.join(ndjson_dir, filename)
            json_file = os.path.join(json_dir, filename.replace('.ndjson', '.json'))
            convert_single_file(ndjson_file, json_file)

    print("Conversion complete.")

def convert_single_file(ndjson_file, json_file):
    with open(ndjson_file, 'r') as ndfile:
        json_data = []
        for line in ndfile:
            json_data.append(json.loads(line))

    with open(json_file, 'w') as jfile:
        json.dump(json_data, jfile)

    print(f"Converted NDJSON file '{ndjson_file}' to JSON file '{json_file}'.")

ndjson_dir = 'D:\\Data\\newJson\\ndjson'
json_dir = 'D:\\Data\\newJson\\jsonlvl1'

print('Converting...')
convert_ndjson_to_json(ndjson_dir, json_dir)
print('Done!')
