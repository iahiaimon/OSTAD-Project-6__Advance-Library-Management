from save_rented_book import save_rented_book 
import datetime
from save_all_book import save_all_book , store

def rent_book(all_book , rented_book):

    title = input("Enter the name or the ISBN number : ").title()

    book_found = True

    for book in all_book:
        if book['name'] == title or book['isbn'] == title:
            print("\n***Book Found***")
            print(f"Do you want to rent the book '{book['name']}' \n")

            print("1: Yes ")
            print("2: No")

            choice = input("\nWhat do you want... ").title()

            if choice == "1" or choice == "Yes" :

                try:
                    while True:
                        p_name = input("\nEnter your name : ")
                        if not p_name:
                            print("\nPlease enter your name ")
                            continue
                        break

                    while True:
                        p_number = input("\nEnter your contact number : ")
                        if not p_number.isdigit():
                            print("\nYou have to enter your numebr for rent the book ")
                            continue
                        break

                    while True:
                        p_title = input("\nEnter the name of the book : ").title()
                        if not p_title or book['name'] != p_title :
                            print("\nEnter the correct name of the book ")
                            continue
                        break

                    name = book['name']
                    author = book['author']
                    isbn = book['isbn']
                    year = book['year']
                    publisher = book['publisher']
                    price = book['price']
                    time = datetime.datetime.now().strftime("%d-%m-%Y -- %H:%M:%S")


                    data = {
                        "borrower_name" : p_name , 
                        "borrower_number" : p_number , 
                        "name": name,
                        "author": author,
                        "isbn": isbn,
                        "year": year,
                        "publisher": publisher,
                        "price": price,
                        "time" : time
                    }

                    rented_book.append(data)
                    save_rented_book(rented_book)
                    print(f"\nYou have successfully rented the book '{book['name']}'")

                    book['status'] = 'rented'
                    all_book.remove(book)
                    save_all_book(all_book)
                
                except Exception as e :
                    print("\nSomething went wrong ")
                    print(f"error is {e}\n")
            
            elif choice == "2" or choice == "No" :
                print("\nThe book is still in the library")
                return all_book
    
    if not book_found:
        print("\nThe book is not found in the library ")
