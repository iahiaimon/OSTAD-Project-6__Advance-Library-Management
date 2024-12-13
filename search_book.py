

def search_book(all_book):
    name = input("Enter the name or the ISBN nunber of the book... ").title()
    
    book_found = False

    for book in all_book:
        if book["name"] == name or book["isbn"] == name :
            print(f"***Book Found***")
            print(f"\nName | {book['name']} , Auther | {book['author']} , ISBN | {book['isbn']} , Year | {book['year']} , Publisher | {book['publisher']} , Price | {book['price']} , Time | {book['time']}")
            book_found = True
            break
    
    if not book_found:
        print(f"The book {name} is not found in the library")
    
    return all_book