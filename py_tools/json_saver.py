import json
import os
from datetime import datetime


def save_json(data, name, destination_folder='JSON', debug=False):
    
    path = os.path.join("static", destination_folder, name, datetime.now().strftime("%m-%d-%Y"))
    
    os.makedirs(path, exist_ok=True)


    file_path = os.path.join(path, f'{name}.json')

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    if debug:
        print(f"Saved JSON files to the '{destination_folder}' folder.")
    return file_path

def main() -> None:
    save_json({'name': 'John Doe', 'age': 30, 'city': 'New York'}, 'person', debug=True)

if __name__ == '__main__':
    main()