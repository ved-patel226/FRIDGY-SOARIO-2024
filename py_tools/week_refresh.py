from datetime import datetime
from termcolor import cprint
import shutil

try:
    from .mongo_db_editor import MongoDBEditor
except:
    from mongo_db_editor import MongoDBEditor

def sunday_check(name: str) -> None:
    today = datetime.now()
    is_sunday = today.weekday() == 6

    mongo = MongoDBEditor("fridgy", "json-data")
    
    if is_sunday:
        mongo.delete_many({"name": name})
        try:
            shutil.rmtree(f"static/Fridge-IMGS/{name}/")
        except:
            pass
        
        cprint("Deleted all entries.", "green", attrs=["bold"])
    else:
        cprint("Not Sunday. No entries deleted.", "red", attrs=["bold"])



def main() -> None:
    sunday_check("ved-patel226")

if __name__ == '__main__':
    main()