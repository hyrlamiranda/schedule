### 08 / 02 / 2017
### Hyrla Miranda
### Otherways to loop through a dictionary

birthday_months = {
	'tony' : 'november',
	'philip': 'june',
	'mary' : 'may',
}

for name in birthday_months.keys():
	print(name.title())

for months in birthday_months.values():
	print(months.title())

for months in set(birthday_months.values()):
	print(months.title())