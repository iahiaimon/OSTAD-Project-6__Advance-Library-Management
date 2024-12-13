from save_all_book import save_all_book

def remove_book(all_book):
    name = input("Enter the ISBN number or the name : ")

    book_found = False

    for book in all_book:

        if book['isbn'] == name or book['name'] == name:

            print(f"Do you want to remove {book['name']} permanently ")
            print("This action cannot be undo\n")
            print("1: Yes")
            print("2: No")

            choice = input("What do you want to do... ").title()

            if choice == "1" or choice == "Yes" :
                all_book.remove(book)
                save_all_book(all_book)
                print(f"The book '{book['name']}' deleted successfully! ")
                book_found = True
                break

            elif choice == "2" or choice == "NO" :
                print(f"The book '{book['name']}' is not removed ")
                break
            
        
    if not book_found :
        print(f"The book {book['name']} is not found in your library")

    return all_book
