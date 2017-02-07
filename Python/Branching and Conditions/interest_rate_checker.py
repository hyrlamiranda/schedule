### 06 / 02 / 2017
### Hyrla Miranda
###Interest rate checker using if-elif-else

# Get user balance
balance = input("What is your bank balance?")

if int(balance) <= 0
	print("Would like to make a deposit.")
elif int(balance <= 50):
	print("You don't qualify for interest.")
elif int(balance) < 100:
	print("Your interest rate is 1%.")
else:
	print("You intereset rate is 2%.")