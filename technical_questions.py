# git
## 1. What is a commit message and why are they important?
### Commit messages are sent with each commit you make to a repository. 
### They're important because they allow other team members to see what code was changed and what was accomplished in your work.

## 2. What is a "git conflict"?
### A git conflict arises when there are two separate branches that have made edits to the same line in a file, 
### or if a file has been deleted in a branch but edited in another. Conflicts must be manually resolved before the branch can be merged into main.

## 3. What is "git stash"?
### Git stash takes a working directory and saves a copy of the changes so that you can reapply at any time if you need to.


# python challenge
##  Write a function that takes a string input: 'str'
##  Return the number / count of vowels in the input string.
##  For the purpose of this assignment, consider 'a', 'e', 'i', 'o' and 'u'
##  as vowels
##  the input string will consist of lower case letters

## Pseudocode Solution
# def count_the_vowels(str):
    # initialize a counter variable  to 0
    # loop through each character in the string
    #  if the char matches one of the  vowels in upper case of lowercase

    # increment counter by one
    # return  the  counter

## python solution
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
## 1. What is Python Pandas?
### Pandas is an open-source library providing easy-to-use data analysis tools for Python.

## 2. What are two different types of data structures in Pandas?
### Series
### Data frame

## 3. What is a data series?
### A Series is a one-dimensional labeled array which holds data of any type (integer, string, objects etc.).

## 4. Define DataFrame in Pandas.
### A DataFrame is a type of data structure in Pandas that works with a two-dimensional array with labeled axes (rows and columns).

## 5. What is re-indexing in Pandas?
### Re-indexing means to conform the DataFrame to a new index. 
### It changes the row labels and column labels.

## 6 . How can we create a copy of a series in Pandas?
### pandas.Series.copy Series.copy(deep=True)

# APIs
## 1. Explain what REST is?
### REST stands for Representational State Transfer.

## 2. What are some common HTTP methods supported by REST and when do you use them?
### GET—requesting a resource. POST—submitting new information. PUT—updates an entire resource. 
### PATCH—updates a partial resource. DELETE—removes a resource.

## 3 . What is the most popular to represent data transfer in a restful API?
### JSON and XML