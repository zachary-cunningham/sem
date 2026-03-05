from book import Book
import sqlite3
import os.path

# build a path from working directory, add bookds.db to the end
db_path = os.path.join(os.path.realpath(
	os.path.join(os.getcwd(), os.path.dirname(__file__))), 'books.db')

# automatically closes, w context manager
def setup_db():
	with sqlite3.connect(db_path) as conn:
		c = conn.cursor()
		c.execute('''CREATE TABLE if not exists books(
			title TEXT,
			pages INTEGER
			)
		''')

setup_db()

# context manager will automatically commit!
def add_book(book):
	with sqlite3.connect(db_path) as conn:
		c = conn.cursor()
		c.execute('INSERT INTO books VALUES (?, ?)', (book.title, book.pages))
		return c.lastrowid

# add_book(Book('$100M Mindset', 169))

def get_books():
	with sqlite3.connect(db_path) as conn:
		c = conn.cursor()
		result = c.execute('SELECT * FROM books').fetchall()
		return [Book(book[0], book[1]) for book in result]

print(get_books())

def get_book_by_title(title):
	with sqlite3.connect(db_path) as conn:
		c = conn.cursor()
		result = c.execute('SELECT * FROM books WHERE title = ?', (title,)).fetchone()
		if result:
			return Book(result[0], result[1])
		return None

# print(get_book_by_title('$100M Offers'))

def delete_book_by_title(title):
	with sqlite3.connect(db_path) as conn:
		c = conn.cursor()
		result = c.execute('DELETE FROM books WHERE title = ?', (title,))
		return c.rowcount

delete_book_by_title('$100M Mindset')

def delete_book(book):
	with sqlite3.connect(db_path) as conn:
		c = conn.cursor()
		result = c.execute('DELETE FROM books WHERE title = ?', (book.title,))
		return c.rowcount