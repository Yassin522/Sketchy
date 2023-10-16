import os
import json
import random
def merge_json(dir1, dir2, output_folder, sample_size):
    os.makedirs(output_folder, exist_ok=True)
    files1 = os.listdir(dir1)
    files2 = os.listdir(dir2)
    files1 = [f for f in files1 if f.endswith('.json')]
    files2 = [f for f in files2 if f.endswith('.json')]
    random.shuffle(files1)
    random.shuffle(files2)

    files1 = files1[:sample_size]
    files2 = files2[:sample_size]

    for file1, file2 in zip(files1, files2):
        json_file1 = os.path.join(dir1, file1)
        json_file2 = os.path.join(dir2, file2)

        with open(json_file1, 'r' , encoding='utf-8') as f1, open(json_file2, 'r',encoding='utf-8') as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)

        data1['drawings'].update(data2['drawings'])

        output_file = os.path.join(output_folder, file1)
        with open(output_file, 'w') as file:
            json.dump(data1, file)


def get_folder_paths(folder):
    folder_paths = []
    for root, folders, files in os.walk(folder):
        for folder in folders:
            folder_path = os.path.join(root, folder)
            folder_paths.append(folder_path)
    return folder_paths

directory1 = 'D:\\Project2\\drawing_ml16\\data\\raw'
directory2 = 'D:\\Data\\newJson\\rawdata'
num_samples = 496
output_folder = 'D:\\Project2\\drawing_ml16\\data\\raw'
sample_size = 496
folders=get_folder_paths(directory2)
print(folders)
for selected_folder in folders:
    print('Merging...')
    merge_json(directory1, selected_folder, output_folder, sample_size)
    print('Done!'+selected_folder)
