### 22/ 02 / 2017
### Hyrla Miranda
### Removing values from a list

books = ['big data', 'checklists', 'the firm', 'tesla', 'the firm', 'the firm']

while 'the firm' in books:
	books.remove('the firm')
	
print(books)