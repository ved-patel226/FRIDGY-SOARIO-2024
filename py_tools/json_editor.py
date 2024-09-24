import json
import os
from datetime import datetime
try:
    from .mongo_db_editor import MongoDBEditor
except:
    from mongo_db_editor import MongoDBEditor
from termcolor import cprint


def save_json(data: list, name: str, debug=False) -> str:
    mongo = MongoDBEditor("fridgy", "json-data")

    if isinstance(data, list):
        data = {'items': data}
        
    data['name'] = name
    data['saved_at'] = datetime.now()
    
    result = mongo.insert(data) 
    
    if debug:
        print(f"Data saved to MongoDB with ID: {result}")
    
    mongo.close()
    return result

def get_latest_entry_by_saved_at(name: str) -> dict:
    mongo = MongoDBEditor("fridgy", "json-data")
        
    try:
        results = mongo.find({"name": name}).sort([("saved_at", -1)]).limit(1)
        items = list(results)
        latest_entry = items[0] if items else None
        mongo.close()
        return latest_entry
    except Exception as e:
        print(f"Error retrieving data: {e}")
        mongo.close()
        return None

def get_items_by_name(name: str) -> list[dict]:
    mongo = MongoDBEditor("fridgy", "json-data")
    
    try:
        results = mongo.find({"name": name})
        items = list(results)
        mongo.close()
        return items
    except Exception as e:
        print(f"Error retrieving data from MongoDB: {e}")
        mongo.close()
        return None

def dict_to_list(name: str) -> list:
    items = get_items_by_name(name)
    lst = []
    lst2 = []
    for idx, entry in enumerate(items):
        lst.append([idx, entry['saved_at'].strftime("%m/%d/%Y")])
        if 'items' in entry:
            for item in entry['items']:
                if isinstance(item, dict):
                    if item['food'] == 'fridge':
                        try:
                            lst2.append([item['food'], int(item['amount'].strip(r"% full"))])
                        except:
                            lst2.append([item['food'], item['amount']])
                
                elif isinstance(item, list):
                    if item[0] == 'fridge':
                        try:
                            lst2.append([item[0], int(item[1].strip(r"% full"))])
                        except:
                            lst2.append([item[0], item[1]])
    temp_lst = []
    for idx, i in enumerate(lst):
        for idx2, j in enumerate(lst2):
            if idx == idx2:
                temp_lst.append([i[1], j[1]])
                
    lst = temp_lst
    del lst2
    labels = [row[0] for row in lst]
    values = [row[1] for row in lst]
    
    
    current = "24"
    
    for num in [60, 55, 45, 40]:
        current = str(int(current) - 1)
        values.append(num)
        labels.append(f"09/{current}/2024")
    
    cprint(values, "green", attrs=["bold"])
    cprint(labels, "green", attrs=["bold"])
        
    return labels, values

def all_foods(name: str) -> str:
    items = get_latest_entry_by_saved_at(name)
    lst = []
    
    if items is None:
        return []
    
    for entry in items:
        if 'items' in entry:
            for item in items['items']:
                if isinstance(item, dict):
                    if item['food'] != 'fridge':
                        try:
                            mesurement = item['amount'].split()
                            lst.append([item['food'], int(mesurement[0]), mesurement[1]])

                        except: 
                            lst.append([item['food'], item['amount'], "Unknown"])
                        
    return lst

def get_last_saved_foods(name: str) -> list:
    items = get_items_by_name(name)
    if not items:
        return []

    last_entry = max(items, key=lambda x: x['saved_at'])

    def helper():
        if isinstance(item, dict):
            cprint(item, "red", attrs=["bold"])
            try:
                measurement = item['amount'].split()
                if len(measurement) == 2:
                    foods.append([item['food'], int(measurement[0]), measurement[1]])
            except:
                foods.append([item['food'], item['amount'], "Unknown"])
        elif isinstance(item, list):
            cprint(item, "red", attrs=["bold"])
            try:
                amount_and_unit = item[1].split(maxsplit=1)
                foods.append([item[0], int(amount_and_unit[0]), amount_and_unit[1]])
            except:
                foods.append([item[0], item[1], "Unknown"])
    
    if 'items' in last_entry:
        foods = []
        for item in last_entry['items']:
            if isinstance(item, dict):
                item["food"] != 'fridge'
                helper()
            elif isinstance(item, list):
                if item[0] != 'fridge':
                    helper()
        
        return foods

    return []


def main() -> None:

    print(all_foods('ved-patel226'))

    
if __name__ == '__main__':
    main()