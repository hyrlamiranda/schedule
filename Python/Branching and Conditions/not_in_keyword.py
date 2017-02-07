### 06 / 02 / 2017
### Hyrla Miranda
### Checking if a value is NOT in a list


# Admin users
admin_users = ['tony', 'frank']

# Ask for username
username = input("Please enter your username?")

# Check if user is a admin user
if username not in admin_users:
	print("You do not have access.")
else:
	print("Access granted.")