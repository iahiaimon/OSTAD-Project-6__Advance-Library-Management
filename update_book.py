import datetime
from save_all_book import save_all_book , store

def update_book(all_book):
    name = input("Enter the name or ISBN number of the book: ").title()

    # all_book = store()

    book_found = False

    for book in all_book:
        if book['name'] == name or book['isbn'] == name:
            print("\n*** Book Found ***")
            print(f"Updating details for '{book['name']}'")
            book_found = True

            try:

                while True:
                    new_name = input("\nEnter the updated name of the book (or press Enter to keep it as is): ").title()
                    if not new_name.strip():
                        new_name = book['name']  
                    break

                while True:
                    new_author = input("\nEnter the updated author's name (or press Enter to keep it as is): ").title()
                    if not new_author.strip():
                        new_author = book['author'] 
                    break

                while True:
                    new_isbn = input("\nEnter the updated ISBN (or press Enter to keep it as is): ")
                    if not new_isbn.strip():
                        new_isbn = book['isbn']
                    elif not new_isbn.isdigit():
                        print("Invalid input! Please enter the ISBN number ")
                        continue
                    elif any(book['isbn'] == new_isbn for book in all_book if book != book):
                        print(f"Another book already has the ISBN '{new_isbn}'. Please enter a unique ISBN ")
                        continue
                    break

                while True:
                    new_year = input("\nEnter the updated year of publication (or press Enter to keep it as is): ")
                    if not new_year.strip():
                        new_year = book['year'] 
                    elif not new_year.isdigit():
                        print("Invalid input! Enter a valid year.")
                        continue
                    break

                while True:
                    new_publisher = input("\nEnter the updated publisher's name (or press Enter to keep it as is): ").title()
                    if not new_publisher.strip():
                        new_publisher = book['publisher'] 
                    break

                while True:
                    try:
                        new_price = input("\nEnter the updated price of the book (or press Enter to keep it as is): ")
                        if not new_price.strip():
                            new_price = book['price'] 
                            break
                        new_price = float(new_price)
                        if new_price < 0:
                            print("Price cannot be negative. Please try again.")
                            continue
                    except ValueError:
                        print("Invalid input! Please enter a numeric value for the price.")
                        continue
                    break

                new_time = datetime.datetime.now().strftime("%Y-%m-%d -- %H:%M:%S")

                books= {
                    "name" : new_name,
                    "author" : new_author ,
                    "isbn" : new_isbn,
                    "year" : new_year,
                    "publisher" : new_publisher,
                    "price" : new_price,
                    "time" : new_time
                }
                book.update(books)
                save_all_book(all_book)

                print(f"\nThe book '{book['name']}' has been updated successfully as {new_name}")
                break

            except Exception as e:
                print(f"An error occurred while updating the book: {e}")
                return all_book

    if not book_found:
        print("\nThe book is not found in your library.")
    return all_book
