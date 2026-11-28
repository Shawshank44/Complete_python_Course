# Library Management System

class Library:
	def __init__(self):
		self.noBooks = 0
		self.Books = []
	def addBook(self, book):
		self.Books.append(book)
		self.noBooks = len(self.Books)
	def showInfo(self):
		print(f"The Library has {self.noBooks} books and the books are : ")
		for book in self.Books:
			print(book)

l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("Complete C programming")
l1.addBook("tarzan")
l1.addBook("jungle book")
l1.addBook("Javascript for noobs")
l1.showInfo()
