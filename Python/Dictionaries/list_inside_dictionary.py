### 08 / 02 / 2017
### Hyrla Miranda
### List inside in Dictionary

my_ordered_car = {
	'type' : 'standard four saloon',
	'extras': ['alloy wheels', 'climate control', 'leather hearted seats']
}

# Print order summat

print("The car you ordered is a " + my_ordered_car['type'] + " with the following extras:")

for extra in my_ordered_car['extras']:
	print("\t" + extra.title())