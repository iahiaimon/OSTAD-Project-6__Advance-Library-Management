# from save_rented_book import rent_store

# rented_book = rent_store()

# def rent_book_list(rented_book):
#     if rented_book != []:
#         total_rent = len(rented_book)
#         print(f"You have {total_rent} rented book")
        
#         for book in rented_book:
#             print(f"\nName | {book['name']} , Auther | {book['author']} , ISBN | {book['isbn']} , Year | {book['year']} , Publisher | {book['publisher']} , Price | {book['price']} , Time | {book['time']}")
    
#     else:
#         print("\n Your rented book list is empty")


# def view(rented_book):
#     rented_book = rent_store()

#     for book in rented_book:
#         print(book)





# import json
# import os

# def load_rented_books():
#     """Loads the list of rented books from rented_book.json."""
#     if not os.path.exists("rented_book.json"):
#         with open("rented_book.json", "w") as file:
#             json.dump([], file)
#         return []

#     with open("rented_book.json", "r") as file:
#         return json.load(file)

# def rent_book_list():
#     """Displays the list of all rented books."""
#     rented_books = load_rented_books()

#     if not rented_books:
#         print("\nNo books are currently rented.")
#         return

#     print(f"\nCurrently, there are {len(rented_books)} rented books:")
#     for idx, book in enumerate(rented_books, start=1):
#         print(f"\nRented Book #{idx}:")
#         print(f"  Borrower's Name    : {book['name']}")
#         print(f"  Contact Number     : {book['number']}")
#         print(f"  Book Title         : {book['title']}")
#         print(f"  Rented On          : {book['time']}")





from save_rented_book import rent_store

rented_book = rent_store()

def rent_book_list(rented_book):

    available_books = [data for data in rented_book if data.get('status', 'available') == 'available']

    if available_books:

        total_book = len(available_books)
        print(f"\nYou have {total_book} books in your library")

        for data in available_books:
            print(f"\nName | {data['name']} , Author | {data['author']} , ISBN | {data['isbn']} , Year | {data['year']} , Publisher | {data['publisher']} , Price | {data['price']} , Time | {data['time']}")
    else:
        print("\nYour rented book list is empty ")

def view(rented_book):

    rented_book = rent_store()

    for data in rented_book:
        print(f"Name: {data['name']}, Author: {data['author']}, ISBN: {data['isbn']}, Year: {data['year']}, Publisher: {data['publisher']}, Price: {data['price']}, Time: {data['time']}, Status: {data.get('status', 'available')}")
