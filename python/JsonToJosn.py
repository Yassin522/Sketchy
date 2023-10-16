import os
import json

def convert_json_directory(input_directory, output_directory):
    json_files = [file for file in os.listdir(input_directory) if file.endswith('.json')]

    os.makedirs(output_directory, exist_ok=True)

    for json_file in json_files:
        input_file = os.path.join(input_directory, json_file)
        output_file = os.path.join(output_directory, json_file)
        converted_data = convert_json(input_file)
        with open(output_file, 'w') as file:
            json.dump(converted_data, file)

        print(f"Converted data saved to '{output_file}'.")

def convert_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    converted_data = []
    students_count = 1

    for entry in data:
        if entry['word']=='t-shirt':
            word='t_shirt'
        else:
            word = entry['word']
            
        session = entry['key_id']
        student = generate_unique_student_name(students_count)
        drawing = convert_strokes(entry['drawing'])

        converted_entry = {
            'session': session,
            'student': student,
            'drawings': {
                word: drawing
            }
        }
        converted_data.append(converted_entry)
        students_count += 1

    return converted_data

def convert_strokes(strokes):
    converted_strokes = []

    for stroke in strokes:
        x_coords = stroke[0]
        y_coords = stroke[1]
        converted_stroke = [[x, y] for x, y in zip(x_coords, y_coords)]
        converted_strokes.append(converted_stroke)

    return converted_strokes

def generate_unique_student_name(count):
    student_name = f"Student{count}"
    return student_name

input_directory = 'D:\\Data\\newJson\\jsonlvl1'
output_directory = 'D:\\Data\\newJson\\raw_json'
print('Converting...')
convert_json_directory(input_directory, output_directory)
print('Done!')