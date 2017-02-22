### 20/ 02 / 2017
### Hyrla Miranda
### Using while loop to quit a program

prompt = "\nTo end this program enter 'q'."
prompt += "\nPlease enter your name: "
message = ""
while message != 'q':
    message = input(prompt)
    print(message)
