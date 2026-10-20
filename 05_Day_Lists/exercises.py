# 💻 Exercises: Day 5
# Exercises: Level 1
# Declare an empty list
list = []
# Declare a list with more than 5 items
list = [1,2,3,4,5,6]
# Find the length of your list
print(len(list))
# Get the first item, the middle item and the last item of the list
first = list[0]
middle = list[3]
last = list[-1]
print(first)
print(middle)
print(last)
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_dt = ['Danny',26,170,'single','ak 9 131 04']
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
# Print the list using print()
print(companies)
# Print the number of companies in the list
print(len(companies))
# Print the first, middle and last company
print(companies[0])
# Print the list after modifying one of the companies
companies[0] = 'Placer.ai'
print(companies)
# Add an IT company to it_companies
companies.append('SpaceX')
print(companies)
# Insert an IT company in the middle of the companies list
companies.insert(3,'Disney')
print(companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
companies[-1] = companies[-1].upper()
print(companies)
# Check if a certain company exists in the it_companies list.
print('Nike' in companies)
# Sort the list using sort() method
companies.sort(reverse=True)
print(companies)
# Reverse the list in descending order using reverse() method
companies.reverse()
print(companies)
# Slice out the first 3 companies from the list
print(companies[:3])
# Slice out the last 3 companies from the list
print(companies[-3:])
# Slice out the middle IT company or companies from the list
print(companies[4])
# Remove the first IT company from the list
del companies[0]
print(companies)
# Remove the middle IT company or companies from the list
del companies[4]
print(companies)
# Remove the last IT company from the list
del companies[-1]
print(companies)
# Remove all IT companies from the list
companies.clear()
print(companies)
# Destroy the IT companies list
del companies
# print(companies)
# Join the following lists:
#
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
comp = front_end + back_end
print(comp)
full_stack = comp.copy()
print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort(reverse=False)
print(ages)
print(ages[0])
print(ages[-1])
# Add the min age and the max age again to the list
ages.append(19)
ages.append(26)
print(ages)
# Find the average age (sum of all items divided by their number )
sum = 0
for age in ages:
    sum = sum + age
average = sum/len(ages)
print(average)
# Find the range of the ages (max minus min)
ages.sort()
min = ages[0]
max = ages[-1]
print(max-min)
# Compare the value of (min - average) and (max - average), use abs() method
abs1 = abs(min-average)
abs2 = abs(max-average)
print(abs1)
print(abs2)
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
chi, rus, usa, *scandic = countries
print(chi)
print(rus)
print(usa)
print(scandic)
