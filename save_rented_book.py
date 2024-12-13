import json , os

def save_rented_book(rented_book):
    with open("rented_book.json" , "w") as myfile:
        json.dump(rented_book , myfile , indent=4)



def rent_store():
    if not os.path.exists("rented_book.json"):

        with open("rented_book.json" , "w") as store_rented:
            json.dump([] , store_rented)
        return[]
    
    with open("rented_book.json" , mode="r") as store_rented:
        return json.load(store_rented)
