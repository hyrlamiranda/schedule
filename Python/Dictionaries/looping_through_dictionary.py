### 08 / 02 / 2017
### Hyrla Miranda
### Looping through a dictionary

birthday_months = {
	'tony' : 'november',
	'philip': 'june',
	'carl' : 'may',
}

for key, value in birthday_months.items():
	print("\nName: " + key.title())
	print("Month: " + value.title())

# Looping through key-value pairs
book_1 = {
	'name' : 'oscar wilde',
	'author' : 'Lady Windermere\'s Fan',
	'price' : '14.99',
	'publisher' : '1893',
}

for key, value in book_1.items():
	print("\nKey: " + key)
	print("Value: " + value.title())

