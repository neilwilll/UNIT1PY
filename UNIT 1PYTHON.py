#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("hello")


# In[4]:


print("John")


# In[ ]:


# Let's assign variables to represent a book you enjoy.

# Step 2 - Strings
# Let's start with Python strings. Replace the "None" with the name of a book, and below the name of the author of your book.

book_name = "Dune"
author = "Frank Herbert"
# book_name = "Dune"
# author = "Frank Herbert"


# Step 3 - Concatenation and f-strings
# Use concatenation and f-strings to make a sentence about your author and book name.

sentence1 = "Dune" + "The top 10 book of all time" + "Frank Herbert"
print(sentence1)
# sentence1 = book_name + " is written by " + author + "."
sentence2 = "Frank Herbert"+"Dune "
print(sentence2)
# sentence2 = f"Author, {author}, wrote the book {book_name}."


# Step 4 - Integers
# Now let's practice Integers. Replace the "None" below with the publication date of your book.
publication_year = 1965
# publication_year = 1965
print(publication_year)

# Step 5 - Floats
# Now estimate what the retail value of your book would be at a store and replace the "None" below with a float value of the price. (Doesn't have to be accurate.)
book_price = 1000.00
# book_price = 17.99
print(book_price)


# Step 6 - Booleans
# Now we will practice with booleans. Replace the "is_awesome" variable with a boolean. True if your book is awesome, False if your book is not awesome.
is_awesome = True
# is_awesome = True
print(is_awesome)


# Step 7 - print and type functions
# Follow the instructions, and below this line, code all of the suggested print statements and the type statements.
# Code below

_authors = [
     "F.Scott Fitzgerald",
     "J.K. Rowling",
     "George R. R. Martin",
     "Ernest Hemingway",
     "Emily Dickenson",
     "George Orwell",
     "Ray Bradbury"
]
my_authors = [
    "Denzel washington",
    "Jason Statham",
    "Leonardo DiCaprio",
    "Jamie Foxx",
    "Samuel L jackson",
    "Al Pacino",
    "Ice Cube"
]
my_authors.append("Kevin Hart")
print(my_authors)

my_authors = [
    "Denzel washington",
    "Jason Statham",
    "Leonardo DiCaprio",
    "Jamie Foxx",
    "Samuel L jackson",
    "Al Pacino",
    "Ice Cube"
]
my_authors.remove("Ice Cube")
print(my_authors)

my_authors = [
    "Denzel washington",
    "Jason Statham",
    "Leonardo DiCaprio",
    "Jamie Foxx",
    "Samuel L jackson",
    "Al Pacino",
    "Ice Cube"
]
my_authors.pop()
print(my_authors)

my_authors = [
    "Denzel washington",
    "Jason Statham",
    "Leonardo DiCaprio",
    "Jamie Foxx",
    "Samuel L jackson",
    "Al Pacino",
    "Ice Cube"
]
print(my_authors[0])

my_authors = [
    "Denzel washington",
    "Jason Statham",
    "Leonardo DiCaprio",
    "Jamie Foxx",
    "Samuel L jackson",
    "Al Pacino",
    "Ice Cube"
]
print(my_authors[1:4])

my_authors_tuple = (
     "Denzel washington",
    "Jason Statham",
    "Leonardo DiCaprio",
    "Jamie Foxx",
    "Samuel L jackson",
    "Al Pacino",
    "Ice Cube"
)

my_authors_set = {
    "Denzel washington",
    "Jason Statham",
    "Leonardo DiCaprio",
    "Jamie Foxx",
    "Samuel L jackson",
    "Al Pacino",
    "Ice Cube"
    }
    
my_authors_set.add("Ice Cube")
print(my_authors_set)
    
    #pt 3
    
#def book_parser():
    #pass

#def book_parser(book_dictionary):
    #pass
    
#def book_parser(book_dictionary):
    # code goes here
    #book_string = f"a book should not be long"

    
def book_parser(book_dictionary):
    book_string = f"Create this string to make the info about the book easy to read."
    return book_string
    
    book_parser(my_book)
    
    #pt 4
    title = input("Money Train name of book? - ")
    author = input("Skip Bayless author")
    year = input("1933 year published ")
    rating = input("5 star rating book - ")
    pages = input("100 pages is the page count of the book? - ")
    
    
    
    book_dictionary = {
      "title": title,
      "author":author,
      "year":year,
      "rating":rating,
      "pages":pages
       }

    return book_dictionary

try:
    year = int(input("1933 is the year was this book published? - "))
except:
    year = int(input("1933 "))

    with open("library.txt", "w") as f:
      f.write("scarface, bob hayes, 1992, 5 star rating,  100 pages\n")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




