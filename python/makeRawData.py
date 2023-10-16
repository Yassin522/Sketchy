import os
import json
import random

def split_json(json_file, output_folder, sample_size=496):
    with open(json_file, 'r') as file:
        data = json.load(file)

    os.makedirs(output_folder, exist_ok=True)

    sampled_data = random.sample(data, sample_size)

    for entry in sampled_data:
        student = entry['student']
        filename = f"{student}.json"
        output_file = os.path.join(output_folder, filename)

        with open(output_file, 'w') as file:
            json.dump(entry, file)


def apply_script_to_directory(input_directory, output_directory, sample_size=496):
    json_files = [file for file in os.listdir(input_directory) if file.endswith('.json')]

    for json_file in json_files:
        input_file = os.path.join(input_directory, json_file)
        output_folder = os.path.join(output_directory, json_file.split('.')[0])
        
        os.makedirs(output_folder, exist_ok=True)
        
        split_json(input_file, output_folder, sample_size)

        print(f"Processed file: {input_file}")

input_directory = 'D:\\Data\\newJson\\raw_json'
output_directory = 'D:\\Data\\newJson\\rawdata'
sample_size = 496

print("Applying script to directory...")
apply_script_to_directory(input_directory, output_directory, sample_size)
print("Done!")