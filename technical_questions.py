# git
    # 1. What is a commit message and why are they important?
        # Commit messages are sent with each commit you make to a repository. 
        # They're important because they allow other team members to see what code was changed and what was accomplished in your work.

    # 2. What is a "git conflict"?
        # A git conflict arises when there are two separate branches that have made edits to the same line in a file, 
        # or if a file has been deleted in a branch but edited in another. Conflicts must be manually resolved before the branch can be merged into main.

    # 3. What is "git stash"?
        # Git stash takes a working directory and saves a copy of the changes so that you can reapply at any time if you need to.


# python challenge
    #  Write a function that takes a string input: 'str'
    #  Return the number / count of vowels in the input string.
    #  For the purpose of this assignment, consider 'a', 'e', 'i', 'o' and 'u'
    #  as vowels
    #  the input string will consist of lower case letters

    # Pseudocode Solution
    # def count_the_vowels(str):
        # initialize a counter variable  to 0
        # loop through each character in the string
        # if the char matches one of the  vowels in upper case of lowercase

        # increment counter by one
        # return  the  counter

    # python solution
def count_the_vowels(str):
    # initialize a counter variable  to 0
    num_vowels = 0
    # loop through each character in the string
    for char in str:
        #  if the char matches one of the  vowels in upper case of     lowercase
        if char in "aeiouAEIOU":
            # increment counter by one
            num_vowels = num_vowels + 1

        # return  the  counter
        return num_vowels

# pandas
    # 1. What is Python Pandas?
        # Pandas is an open-source library providing easy-to-use data analysis tools for Python.

    # 2. What are two different types of data structures in Pandas?
        # Series
        # Data frame

    # 3. What is a data series?
        # A Series is a one-dimensional labeled array which holds data of any type (integer, string, objects etc.).

    # 4. Define DataFrame in Pandas.
        # A DataFrame is a type of data structure in Pandas that works with a two-dimensional array with labeled axes (rows and columns).

    # 5. What is re-indexing in Pandas?
        # Re-indexing means to conform the DataFrame to a new index. 
        # It changes the row labels and column labels.

    # 6 . How can we create a copy of a series in Pandas?
        # pandas.Series.copy Series.copy(deep=True)

# APIs
    # 1. Explain what REST is?
        # REST stands for Representational State Transfer.

    # 2. What are some common HTTP methods supported by REST and when do you use them?
        # GET—requesting a resource. POST—submitting new information. PUT—updates an entire resource. 
        # PATCH—updates a partial resource. DELETE—removes a resource.

    # 3 . What is the most popular to represent data transfer in a restful API?
        # JSON and XML

# SQL
    # 1. What is SQL and how is it different from NoSQL?
        # SQL databases are held in tables, and are relational; 
        # i.e. tables can be related to other tables in the database. 
        # NoSQL databases are usually document based, where key-value pairs are used to store data.

    # 2. What is a primary key?
        # A primary key is either a single or combination of fields 
        # which uniquely identify a row in the table.

    # 3. What is a foreign key?
        # A foreign key in one table represents the primary key of another table. 
        # The relationship between the two is created by referencing each key.

    # 4. What joins can you tell me about?
        # Inner join: Inner joins return rows where there is at least one match of rows
        # Right join: Returns all the rows from the right hand table, even if there are no matches in the left
        # Left join: Reverse of right join
        # Full join
        # Results in the combination of results from both left and right tables.
        # It will contain all records from both tables.

    # 5. What is a relationship and what kinds are there? 
        # Relationships are the associations between two columns in two or more tables. 
        # Table A will be associated with Table B in different ways. They are:

        # 1. One-to-one
            # Defined as a direct relationship between two tables, 
            # a primary key on Table A will be associated with a foreign key on Table B; 
            # i.e. one author has only one place of birth.
    
        # 2. One-to-many
            # Defined as a relationship between two tables where 
            # a row from Table A matches multiple rows in Table B; 
            # i.e. one author can have many books.

        # 3. Many-to-one
            # The reverse of one-to-many, 
            # where a row from Table B can match multiple from Table A.

        # 4. Many-to-many
            # Defined as a relationship between two tables where 
            # multiple rows from Table A match multiple rows from Table B, 
            # usually through Table C; i.e. where 
            # Table A is a list of application users, 
            # and table B is a list of books, 
            # Table C would combine IDs from both tables to indicate 
            # who owns which books in their personal library.

# ETL
    # 1. What is ETL?
        # ETL stands for Extract, Transform, Load; it is a process for collecting, cleaning, and saving data.
        # The Extract step reads data from disparate data sources, 
        # while the Transform step converts the data into a useful format, 
        # and the Load step writes that data into the target database or data warehouse.
    
    # 2. What are regular expressions and why would you want to use them?
        # Regular expressions are a sequence of specific characters that help match or find other strings, 
        # or sets of strings, using specialized syntax. 
        # Often shortened to "RegEx," they can be used with the Python package "re."

    # 3. Define a lambda function and give an example.
        # A lambda function is a short, anonymous function; 
        # it can take any number of arguments but only has one expression.
        # Compare your example with something offered earlier in this week's material.

# SQLAlchemy
    # Look at the following code snippets, and try to answer the questions accompanying them.

    # Snippet #1

from sqlalchemy.engine.url import URL
postgres_db = {'drivername': 'postgres',
               'username': 'postgres',
               'host': '192.168.99.100',
               'port': 5432}
print(URL(**postgres_db))

        # Question: What line of code is missing from setting up postgres_db with SQLAlchemy?
        # Answer: 'password': '<password>', needs to be included in the setup object.

    # Snippet #2
# Declare a table
table = Table('Example',metadata,
              Column('id',Integer),
              Column('name',String))
        # Question: What line of code would you apply primary_key=True to?
        # Answer: The primary key could technically be either column, 
        # but common practice is to apply it to the id, 
        # so we'd get: Column('id',Integer, primary_key=True)

    # Snippet #3

from sqlalchemy import create_engine
from sqlalchemy import inspect
db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

inspector = inspect(engine)
# Get table information
print(inspector.get_table_names())
# Get column information
print(inspector.get_columns('EX1'))
        
        # Question: What does the above code do?
        # Answer: This code imports "inspect" from SQLAlchemy and uses the inspector 
        # to get the names of all tables and to get all columns from those tables in our database.

# Web scraping
    # Case Studies

# Javascript

# Plotly
    # Case Studies

# JavaScript API
    # 1. What is Leaflet?
        # Leaflet is an extremely popular, open-source JavaScript library for 
        # mobile-friendly interactive maps. It helps us display and visualize data 
        # in ways that are user-friendly and meaningful for data analysts and nonexperts alike.

    # 2. Tell me about your experience using Leaflet?
        # There is no concrete answer here, but the "tell me about" format 
        # is extremely popular in interviews. It is an open-ended question that invites 
        # you to sell your skills! Write down your experiences using Leaflet this week. 
        # What were the challenges? How did you overcome them? 
        # What did you learn that is applicable to the job you're applying for?

    # 3. What is the GeoJSON data format?
        # GeoJSON is an open standard format, which is essentially a type of 
        # JSON (JavaScript Object Notation) for representing geographical features 
        # along with their nonspatial attributes. 
        # It is commonly used with libraries like Leaflet.js.

    # 4.
    #5.
    


