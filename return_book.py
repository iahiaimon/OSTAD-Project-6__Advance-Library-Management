from save_rented_book import save_rented_book 
import datetime
from save_all_book import save_all_book , store

def return_book(all_book , rented_book):

    title = input("Enter the name or the ISBN number : ").title()

    book_found = True

    for data in rented_book:
        if data['name'] == title or data['isbn'] == title:
            print("\n***Book Found***")
            print(f"Do you want to return the book '{data['name']}' \n")

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
                        if not p_title or data['name'] != p_title :
                            print("\nEnter the correct name of the book ")
                            continue
                        break

                    name = data['name']
                    author = data['author']
                    isbn = data['isbn']
                    year = data['year']
                    publisher = data['publisher']
                    price = data['price']
                    time = datetime.datetime.now().strftime("%d-%m-%Y -- %H:%M:%S")


                    return_data = {
                        "name": name,
                        "author": author,
                        "isbn": isbn,
                        "year": year,
                        "publisher": publisher,
                        "price": price,
                        "time" : time
                    }

                    all_book.append(return_data)
                    save_all_book(all_book)
                    print(f"\nYou have successfully return the book '{data['name']}'")

                    rented_book.remove(data)
                    save_rented_book(rented_book)

                except Exception as e :
                    print("\nSomething went wrong ")
                    print(f"error is {e}\n")
            
            elif choice == "2" or choice == "No" :
                print("\nThe book is still in the rented book list")
                return all_book
    
    if not book_found:
        print("\nThe book is not found in the rented book list ")