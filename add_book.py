import datetime
from save_all_book import save_all_book


def add_book(all_book):

    try:
        while True:
            name = input("\nEnter the name of your book: ").title()
            if not name.strip():
                print("Name cannot be empty. Please try again ")
                continue
            break

        while True:
            author = input("\nEnter the name of the author: ").title()
            if not author.strip():
                print("Author name cannot be empty. Please try again ")
                continue
            break

        while True:
            isbn = input("\nEnter the ISBN number: ")
            if not isbn.isdigit():
                print("Invalid input! ISBN must be a numeric value. Please try again ")
                continue

            if any(book['isbn'] == isbn for book in all_book):
                print(f"\nThe book '{name}' is already in your library ")
                return all_book
            break

        while True:
            year = input("\nEnter the year of publication: ")
            if not year.isdigit():
                print("Invalid input! Enter a valid year ")
                continue
            break

        while True:
            publisher = input("\nEnter the name of the publisher: ").title()
            if not publisher.strip():
                print("Publisher name cannot be empty. Please try again ")
                continue
            break

        while True:
            try:
                price = float(input("\nEnter the price of the book: " + "$"))
                if price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid numeric value for the price.")
                continue
            break

        time = datetime.datetime.now().strftime("%d-%m-%Y -- %H:%M:%S")

        book = {
            "name": name,
            "author": author,
            "isbn": isbn,
            "year": year,
            "publisher": publisher,
            "price": price,
            "time": time
        }

        all_book.append(book)

        save_all_book(all_book)

        print(f"Successfully added the new book: '{name}'")

    except Exception as e:
        print("An unexpected error occurred. Please try again.")
        print(f"Error details: {e}")

    return all_book
