from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

DB_PATH = Path("db/shopping_list.json")


class Item(BaseModel):
    name: str
    quantity: int
    



def load_database() -> list:
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")


def save_database(data: list) -> None:
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)



@app.get("/items")
def list_items() -> list:
    data = load_database()
    return data


@app.post("/items")
def create_item(item: Item):
    data = load_database()

    if len(data) == 0:
        new_item_id = 1
    else:
        new_item_id = data[-1]["id"] + 1 # create new id by last item's id plus one, thats way resolve deleting problems
    
    new_item = {"id": new_item_id, "name": item.name,"quantity": item.quantity}
    data.append(new_item)
    save_database(data)
    return new_item





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)