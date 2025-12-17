from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

DB_PATH = Path("db/shopping_list.json")
BACKUP_DB_PATH = Path("data/backup_shopping_list.json")

class Item(BaseModel):
    name: str
    quantity: int
    



def load_database(path) -> list:
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")


def save_database(path, data: list) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2)



@app.get("/items")
def list_items() -> list:
    data = load_database(DB_PATH)
    return data


@app.post("/items")
def create_item(item: Item):
    data = load_database(DB_PATH)

    if len(data) == 0:
        new_item_id = 1
    else:
        new_item_id = data[-1]["id"] + 1 # create new id by last item's id plus one, thats way resolve deleting problems
    
    new_item = {"id": new_item_id, "name": item.name,"quantity": item.quantity}
    data.append(new_item)
    save_database(DB_PATH ,data)
    return new_item




@app.get("/backup")
def list_backup_items() -> list:
    data = load_database(BACKUP_DB_PATH)
    return data


@app.post("/backup/save")
def save_to_backup():
    try:
        data = load_database(DB_PATH)
        save_database(BACKUP_DB_PATH, data)
        return data
    except Exception as err:
        raise {"error": err}

    
        


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)