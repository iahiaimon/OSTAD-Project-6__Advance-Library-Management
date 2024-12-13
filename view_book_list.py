# from save_all_book import store

# all_book = store()

# def view_book_list(all_book):
#     if all_book != []:
#         total_book = len(all_book)
#         print(f"\nYou have {total_book} books in your library")
#         for book in all_book:
            
#             print(f"\nName | {book['name']} , Auther | {book['author']} , ISBN | {book['isbn']} , Year | {book['year']} , Publisher | {book['publisher']} , Price | {book['price']} , Time | {book['time']}")
#     else:
#         print("\nYour book library is empty ")
    
# def view(all_book):
#     all_book = store()

#     for book in all_book:
#         print(book)




from save_all_book import store

all_book = store()

def view_book_list(all_book):

    available_books = [book for book in all_book if book.get('status', 'available') == 'available']

    if available_books:

        total_book = len(available_books)
        print(f"\nYou have {total_book} books in your library")

        for book in available_books:
            print(f"\nName | {book['name']} , Author | {book['author']} , ISBN | {book['isbn']} , Year | {book['year']} , Publisher | {book['publisher']} , Price | {book['price']} , Time | {book['time']}")
    else:
        print("\nYour book library is empty or all books are rented.")

def view(all_book):

    all_book = store()

    for book in all_book:
        print(f"Name: {book['name']}, Author: {book['author']}, ISBN: {book['isbn']}, Year: {book['year']}, Publisher: {book['publisher']}, Price: {book['price']}, Time: {book['time']}, Status: {book.get('status', 'available')}")
