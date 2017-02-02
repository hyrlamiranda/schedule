### 01 / 02 / 2017
### Author: Hyrla Miranda
### How to Edit Lists

# Creating a list of months
birthday_months = ['january' , 'spril', 'june']

# Print our list
print(birthday_months)

# Changing an element of list
birthday_months[1] = 'april'

print(birthday_months)

# Using method append() appends a passed obj into the existing list.
birthday_months.append('december')

print(birthday_months)

# Creating an empty list
birthday_months = []

print(birthday_months)

birthday_months.append('may')

print(birthday_months)

# Using insert() method, inserts object obj into list at offset index.
birthday_months.insert(0,"february")

print(birthday_months)

# Using the delete statement
del birthday_months[1]

print(birthday_months)

