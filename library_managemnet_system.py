class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}
    
    
    
    def add_book(self):
        adding = input('Enter the name of the book: ').strip() .split(',')
        adding = [book.strip() for book in adding]
        added_books = []
        for book in adding:
            if book not in self.books:
                self.books.append(book)
                added_books.append(book)
        if added_books:
            print(f'Books added to the library: {" ,".join(added_books)}')
        else:
            print('no new books were added!')

    def borrow_book(self):
        name = input('Enter the name of the book that you want to borrow: ')
        borrower = input('Enter the name of borrower: ')
        if name in self.books:
            self.borrowed_books[name] = borrower
            self.books.remove(name)
            print(f'{name} borrowed successfully by {borrower}')
        else:
            print('Sorry, this book is not exist in the library')
    
    def return_book(self):
        name = input('Enter the name of book: ')
        borrower = input('Enter the name of the borrower: ')
        if name in self.borrowed_books:

            if self.borrowed_books[name] == borrower:
                self.books.append(name)
                self.borrowed_books.pop(name)
                print(f'the book {name} returned to the library by {borrower}.')
            else:
                print(f'the book {name} is borrowed bofore and can not borrow again')
        elif name not in self.borrowed_books and name in self.books:
            print('this book is in the library and not borrowed by anyone')
    def show_all_books(self):
        print(self.books)
library = Library()
while True:
    print('\n Library system')
    print('1. Add book')
    print('2. Borrow book')
    print('3. Return book')
    print('4. view books')
    print('5. Exit')

    choice = int(input('select your choice: '))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        if library.books:
            library.borrow_book()
        else:
            print('No book available in the library to borrow.')

    elif choice == 3:
        library.return_book()
    elif choice == 4:
        library.show_all_books()
    elif choice == 5:
        break
    else:
        print('Invalid number, please try again!')