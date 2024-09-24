import google.generativeai as gai
from PIL import Image
import pprint
import re
import json
try:
    from .env_translator import env_to_var
    from .json_editor import *
except:
    from env_translator import env_to_var
    from json_editor import *

def get_most_recent_file(directory: str) -> str:
    try:
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except:
        return None
    
    if not files:
        return None
    most_recent_file = max(files, key=os.path.getctime)
    return most_recent_file

def gai_vision(name: str, image_path: str = "static\\Fridge-IMGS") -> str:

    """Returns the JSON file path of the JSON outpu t"""
    """JSON FORMAT: """

    image_path = f"{image_path}\\{name}\\"
    
    
    image_path = get_most_recent_file(image_path)
    
    if image_path == None:
        print("Error: No image found")
        return None
    
    gai.configure(api_key=env_to_var("GEMINI_KEY"))

    img = Image.open(image_path)

    model = gai.GenerativeModel('gemini-1.5-flash')

    foods = get_last_saved_foods(name)
    
    if foods == []:
        prompt = "List all packaged foods currently stored in the fridge along with their estimated amounts. If you are not sure about the amounts, take an educated guess. Also at the end include a percentage of how full the fridge is. 100% being packed and 0% meaning nothing. Don't give ranges for anything"
    else:
        prompt = "List all packaged foods currently stored in the fridge along with their estimated amounts. If you are not sure about the amounts, take an educated guess. Also at the end include a percentage of how full the fridge is. 100% being packed and 0% meaning nothing. Don't give ranges for anything. Here are the previous foods stored in the fridge:\n\n"
        for food in foods:
            prompt += f"- {food}\n"
    
    result = model.generate_content(
        [img, "\n\n", prompt]
    )

    lines = result.text.split('\n')

    lines = [line[3:] if line.startswith('-') else line for line in lines[1:] if line.strip() != '']


    prompt = (
        "Sort the following data into lists of [food, amount] return a JSON. If it is showing the amount the fridge is full, write fridge for the food:\n\n"
        "Here is the data:\n" + '\n'.join(lines) + "\n\n"
    )

    response = model.generate_content(prompt)
    json_str = response.text.replace('```json', '').replace('```', '').strip()
    
    try:
        data = json.loads(json_str)
    except:
        print("Error: Could not parse JSON")
        return None
    
    path = save_json(data, name, debug=True)
    
    return path

def main() -> None:
    gai_vision("ved-patel226", "static\\Fridge-IMGS")

if __name__ == '__main__':
    main()