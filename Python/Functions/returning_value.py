### 23/ 02 / 2017
### Hyrla Miranda
### Returning a value in a function

def formatted_name(first_name, last_name):
	""" Return formatted name"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

student = formatted_name('hyrla', 'miranda')
print(student)

def get_formatted_username(email_address):
	"""Return a formatted username"""
	username = email_address.strip()
	return username
user = get_formatted_username('hyrlammiranda@gmail.com')
print(user)