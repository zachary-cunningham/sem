import sqlite3 # lightweight, distributed database
# for clients, not really servers(Postgres)

conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute('''CREATE TABLE if not exists books(
			title TEXT,
			pages INTEGER
		)
'''
)

# books = [
# 	('$100M Offers', 340),
# 	('$100M Leads', 290),
# 	('$100M Models', 320),
# ]


# # c.execute("INSERT INTO books VALUES ('$100M Models', 140)")

# #conn.commit()
# c.execute("DELETE FROM books")


# c.executemany('INSERT INTO books VALUES (?, ?)', books)

# conn.commit()

c.execute('UPDATE books SET pages=69 WHERE title = "$100M Offers"')

c.execute("SELECT * FROM books")
print(c.fetchall())
