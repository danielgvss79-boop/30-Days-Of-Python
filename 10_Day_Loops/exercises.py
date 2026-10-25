# 💻 Exercises: Day 10
from data.countries import countries
from data.countries_data import data

# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
     print(number)

count=0
while count<11:
    print(count)
    count+=1
else:
    print(f'count stopped at {count}')

# Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(10,-1,-1):
    print(number)

count=10
while count>=0:
    print(count)
    count = count-1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
chars='#######'
output=''
for char in chars:
    output=output+char
    print(output)

# Use nested loops to create the following:
#
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

for x in range(8):
    for y in range(7):
        print('#',end=' ')
    print()

# Print the following pattern:
#
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for number in range(11):
    print(f'{number} x {number} = {number * number}')

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list=['Python', 'Numpy','Pandas','Django', 'Flask']

for language in list:
    print(language)

# Use for loop to iterate from 0 to 100 and print only even numbers

for even in range(1,101):
    if even % 2 == 0:
        print(even)


# Use for loop to iterate from 0 to 100 and print only odd numbers

for odd in range(1,101):
    if odd % 2 != 0:
        print(odd)

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.

sum=0
for number in range(101):
    sum+=number
print(sum)

# The sum of all numbers is 5050.

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even=0
sum_odds=0

for number in range(101):
    if number % 2 == 0:
        sum_even+=number
    else:
        sum_odds+=number
print(sum_even)
print(sum_odds)

# The sum of all evens is 2550. And the sum of all odds is 2500.

# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
selected=[]
for country in countries:
    if 'land' in country:
        selected.append(country)
print(selected)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits=['banana', 'orange', 'mango', 'lemon']
new_fruits=[]
count=0
for fruit in fruits:
    new_fruits.append(fruits[len(fruits)-1-count])
    count= count + 1
print(new_fruits)


# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
unique_languages= set()

for country in data:
    unique_languages.update(set(country['languages']))
print(len(unique_languages))
print(unique_languages)

# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world