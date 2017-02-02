### 02 / 02 / 2017
### Hyrla Miranda
### Organizing a list

# Creating a list of months
birthday_months = ['may', 'november', 'june']

#The method sort() sorts objects of list, use compare func if given.
birthday_months.sort()
print(birthday_months)

#Using the reverse sort method
birthday_months = ['may', 'november', 'june']

birthday_months.sort(reverse=True)
print(birthday_months)

birthday_months = ['may', 'november', 'june']

print(sorted(birthday_months))
print(birthday_months)

birthday_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
birthday_days.reverse()
print(birthday_days)