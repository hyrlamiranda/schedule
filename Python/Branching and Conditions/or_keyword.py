### 06 / 02 / 2017
### Hyrla Miranda
### Using the OR keyword to check values in a list

# Names registered
registered_names = ['tony', 'frank', 'hyrla' , 'camilo', 'chris']

username = input ("Please enter the user name you would like to use.")

# Check to see if username is already taken
if username in registered_names:
	print("Sorry, username already taken.")
else:
	print("This username is available.")