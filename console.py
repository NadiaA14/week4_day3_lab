import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("Matt", "Haig")
author_repository.save(author1)

author2 = Author("Sally", "Rooney")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("The Midnight Library", author1, "A woman who gets to try out different versions of her life", 5)
book_repository.save(book1)

book2 = Book("Normal People", author2, "Follows the friendship of a boy and a girl from highschool to adulthood", 1)
book_repository.save(book2)

book3 = Book("Conversations With Friends", author2, "Two friends doing questionable things with an older married couple", 4)
book_repository.save(book3)

pdb.set_trace()