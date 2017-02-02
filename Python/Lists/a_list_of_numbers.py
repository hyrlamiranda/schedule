### 02 / 02 / 2017
### Hyrla Miranda
### Creating a list of numbers

#The range() function has two sets of parameters, as follows:
#range(stop)
#stop: Number of integers (whole numbers) to generate, starting from zero. eg. range(3) == [0, 1, 2].
#range([start], stop[, step])
#start: Starting number of the sequence.
#stop: Generate numbers up to, but not including this number.
#step: Difference between each number in the sequence.

# Convert numbers in to a list
numbers = list(range(1,6))
print(numbers)

odd_numbers = list(range(1,101 , 5))
print(odd_numbers)

squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)

digits = [1,2,3,4,5]
print(min(digits))

digits = [1,2,3,4,5]
print(max(digits))