class Book:
	favs = []

	@staticmethod
	def read_books_from_file():
		books = []
		try:
			with open('input.txt', 'r') as file:
				data = file.read().split('\n')

			for book in data:
				book_data = book.split('\t')
				if book.strip():
					books.append(Book(book_data[0], int(book_data[1])))
		except FileNotFoundError as e:
			print('file not found', e)
		except Exception as e:
			print('error:', e)
		finally:
			pass
		return books

	@staticmethod
	def write_books_to_file(books):
		file = open('input.txt', 'w')
		for book in books:
			file.write(f'{book.title}\t{book.pages}\n')
		file.close()

    # is invoked whenever instanciating
	def __init__(self, title, pages) -> None:
		self.title:str = title
		self.pages:int = pages
		
    # called when printing
	def __str__(self):
		return f'{self.title}, {self.pages} pages long'

	__hash__ = None # cannot be hashed into a set, or be a key in a dictionary

	def __repr__(self) -> str:
		return str(self)
    
	def __eq__(self, other) -> bool:
		return self.title == other.title and self.pages == other.pages

	def is_short(self):
		return self.pages < 100