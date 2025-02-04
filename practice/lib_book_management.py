# Problem: Library Book Management

# 1. Create a list called library_books that contains the following book titles: "1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Great Gatsby", "Moby Dick".

# 2. Print the entire list of book titles.

# 3. Print the total number of books in the list.

# 4. Add a new book "War and Peace" to the end of the list.

# 5. Remove the book "Moby Dick" from the list.

# 6. Print the modified list and the new total number of books.

library_books = ["1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Great Gatsby", "Moby Dick"]
print(library_books)
print("Books:", len(library_books))

library_books.append("War and Peace")
library_books.remove("Moby Dick")
print(library_books)
