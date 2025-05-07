books = ['1984', 'The Catcher in the Rye', 'To Kill a Mockingbird', 'The Great Gatsby']
more_books = ['The Hobbit', 'Fahrenheit 451']

def find_book(books, target):
    count = 0
    for i in books:
        if i == target:
            books.insert(count, 'Brave New World')
            books.remove(target)
            return
        count += 1
    return

def readBooks(books):
    for i in books:
        print("I Have Read: ", i)
    return

def expandBooks(books, new):
    for i in new:
        books.append(i)
    return books


def change_books(books):
    print(books[0], books[-1])

    books.append('Moby Dick')
    books.insert(2, 'Pride and Prejudice')
    books.remove('The Catcher in the Rye')
    find_book(books, '1984')
    readBooks(books)
    books = expandBooks(books, more_books)
    print(books)
    return books

change_books(books)