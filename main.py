import add_book
from save_all_book import store
import remove_book
import view_book_list
import search_book
import update_book
import rent_book
from save_rented_book import rent_store
import return_book
import rent_book_list

all_book = store()

rented_book = rent_store()

def main():

    while True:

        print("\n***Wlecome to you personal library***")
        print("You can add , remove , update , rent book \n")
        print("1: Add Book ")
        print("2: Remove Book ")
        print("3: Update book ")
        print("4: View Book List ")
        print("5: Search Book ")
        print("6: Rent Book ")
        print("7: Return Book ")
        print("8: Rent Book List ")
        print("0: Exit\n")


        choice = input("Sellect an option : ").title()


        if choice == "1" or choice == "Add Book":
            add_book.add_book(all_book)

        elif choice == "2" or choice == "Remove Book":
            remove_book.remove_book(all_book)

        elif choice == "3" or choice == "Update Book":
            update_book.update_book(all_book)

        elif choice == "4" or choice == "View Book List":
            view_book_list.view_book_list(all_book)

        elif choice == "5" or choice == "Search Book":
            search_book.search_book(all_book)

        elif choice == "6" or choice == "Rent Book":
            rent_book.rent_book(all_book , rented_book)

        elif choice == "7" or choice == "Return Book":
            return_book.return_book(all_book , rented_book)

        elif choice == "8" or choice == "Rent Book List":
            rent_book_list.rent_book_list(rented_book)

        elif choice == "0" or choice == "Exit":
            print("Successfully exited from your library ")
            print("Have a good day!")
            break
        
        else:
            print("\nInvalid input... Please choose an option from the list. ")


if __name__ == "__main__":
    main()






