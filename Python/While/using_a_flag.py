###### 20/ 02 / 2017
### Hyrla Miranda
### Using a flag to stop a program


prompt = "\nEnter 'q' to end this program"
prompt += "\nWhat is your name?"

#set our flag to true
active = True
while active:
     message = input(prompt)

     if message == 'q':
         active = False
     else: 
     	print(message)