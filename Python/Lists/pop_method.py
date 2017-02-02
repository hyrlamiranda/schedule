### 02 / 02 / 2017
### Author: Hyrla Miranda
### Using the pop() method

subcribers = ['hyrla@example.com', 'miranda@example.com', 'example@example.com']
print(subcribers)

#The method pop() removes and returns last object or obj from the list.
popped_subscriber = subcribers.pop()

print(subcribers)

print(popped_subscriber)

subcribers = ['hyrla@example.com', 'miranda@example.com', 'example@example.com']
first_subscriber = subcribers.pop(0)

print("Your first subscriber was " + first_subscriber + ".")

subcribers = ['hyrla@example.com', 'miranda@example.com', 'example@example.com']
print(subcribers)

subcribers.remove("miranda@example.com")

print(subcribers)

subcribers = ['hyrla@example.com', 'miranda@example.com', 'example@example.com']
subscribed_by_mistake = 'hyrla@example.com'
subcribers. remove(subscribed_by_mistake)

print(subcribers)

print( "\nThis person " + subscribed_by_mistake + "did not mean to sign up.")