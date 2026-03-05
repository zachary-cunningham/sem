import books_sdk
from book import Book

def print_menu():
	print('''Choose a number
	1. Print all books
	2. Add a book
	3. Delete a book
	0. Quit''')

print('Welcome to the library!')
while(True):
	print_menu()
	response = int(input())

	# print all books
	if response == 1:
		for book in books_sdk.get_books():
			print(book)

	# add a book
	elif response == 2:
		title = input('Title? ')
		page_count = input('Page count? ')
		books_sdk.add_book(Book(title, page_count))
	# delete a book
	elif response == 3:
		title = input('Title? ')
		books_sdk.delete_book_by_title(title)
		print(f'Deleted {title}')

	# exit
	else:
		print('Thank you for visiting!')
		break