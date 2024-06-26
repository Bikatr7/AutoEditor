import json

def load_genders(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def find_name_gender(name):
    result = []

    genders = load_genders("./instructions/genders.json")
    
    # Check each gender category
    for gender, names in genders.items():
        # Check each full name and partial names in the gender category
        for full_name, parts in names.items():
            if(name in full_name.split() or name in parts):
                result.append(gender)
    
    return result
