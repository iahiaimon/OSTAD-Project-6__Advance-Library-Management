import json
import os

def save_all_book(all_books):
    with open("all_books.json", "w") as myfile:
        json.dump(all_books, myfile, indent=4)

def store():
    if not os.path.exists("all_books.json"):
        with open("all_books.json", "w") as store_file:
            json.dump([], store_file)
        return []
    with open("all_books.json", mode="r") as store_file:
        return json.load(store_file)

