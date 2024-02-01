#!/usr/bin/env python3
import os

source_path = "/Users/peterfsmith/Documents/screenshots"
file_list = os.listdir(source_path)
# print(file_list)

for file in file_list:
    # Check if file ends with '.jpg'
    if file.endswith('.png'):
        if 'Screenshot' in file:
            # Replace 'foo' with 'bar' in the file name
            new_name = file.replace('Screenshot', 'eS')
            # Rename the file using os.rename
            os.rename(os.path.join(source_path, file), os.path.join(source_path, new_name))
            # Print out a confirmation message
            print(f"Renamed {file} to {new_name}")