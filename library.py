import random

class Book:
    def __init__(self, author, name, id: int):
       self.author = author
       self.name = name
       self.id = id
       self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True


class Member:
    def __init__(self, name, member_id: int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.limit = 0

    def take_book(self, book):
        if self.limit < 3:
            if book.borrow_book():
                self.borrowed_books.append(book)
                self.limit += 1
                return True
        else:
            print('Your limit has been reached! Return a book to be able to borrow it!')
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            self.limit -= 1
            return True
        return False



class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)


    def reg_member(self, member):
        self.members.append(member)

    def del_member(self, member_id):
        self.members.remove(Member(member_id=member_id))


    def borrow_book(self, id, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.id == id), None)
        if member and book:
            return member.borrow_book()
        return False

    def return_book(self, id, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.id == id), None)
        if member and book:
            return member.return_book()
        return False



def main():
    library = Library()
    while True:
        print('\nLibrary Management System')
        print('1. Add book')
        print('2. Register a new member')
        print('3. Remove a member')
        print('4. Borrow a book')
        print('5. Return a book')
        print('6. Exit')
        choice = int(input('Enter your choice (type a number): '))

        if choice == 1:
            title = input('Name a title: ')
            author = input('Name an author: ')
            id = input('Give an ID: ')
            book = Book(title, author, id)
            library.add_book(book)
            print(f'Book {title} added successfully!')

        elif choice == 2:
            name = input('What is your name?: ')
            id = input('Give an ID: ')
            member = Member(name, id)
            library.reg_member(member)
            print('A member has been registered successfully!')

        elif choice == 3:
            name = input('Enter a members name: ')
            m_id = int(input('Enter a members ID: '))
            ch = input('Are you sure you wanna delete it? (y/n): ')
            if ch.lower() == 'y':
                member = Member(name, m_id)
                if member in library.members:
                    library.del_member(name)
                    print('A member has been removed successfully!')
            elif ch.lower() == 'n':
                continue

        elif choice == 4:
            m_id = int(input('Enter a members ID: '))
            b_id = int(input('Enter a books ID: '))
            if library.borrow_book(b_id, m_id):
                print('Book has been borrowed! Please, do not forget to return it in time!')
            else:
                print('Book has not been found')

        elif choice == 5:
            m_id = int(input('Enter a members ID: '))
            b_id = int(input('Enter a books ID: '))
            if library.return_book(b_id, m_id):
                print('Book has been returned! See you again!')
            else:
                print('Book has not been found')

        elif choice == 6:
            break

        else:
            print('Invalid type of request!')

if __name__ == '__main__':
    main()