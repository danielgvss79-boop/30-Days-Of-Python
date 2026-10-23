# 💻 Exercises: Day 9

# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = 8
if age>18:
    print('You are old enough to drive')
else:
    print(f'Wait {18-age} years')

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 20
your_age = 20
if my_age>your_age:
    if abs(my_age-your_age)==1:
        print('I win, 1 year')
    else:
        print('I win, years')
elif my_age<your_age:
    if abs(your_age-my_age)==1:
        print('You win, 1 year')
    else:
        print('You win, years')
else:
    print('Same age')


# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```
score=93

if score>=90 and score<=100:
    score='A'
    print(score)
elif score>=80 and score<90:
    score='B'
    print(score)
elif score>=70 and score<80:
    score='C'
    print(score)
elif score>=60 and score<70:
    score='D'
    print(score)
else:
    score='F'
    print(score)

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is:
# September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
winter=['December','January','February']
spring=['March','April','May']
summer=['June','July','August']
fall=['September','October','November']

month='February'

if month in winter:
    print('winter')
elif month in spring:
    print('spring')
elif month in summer:
    print('summer')
elif month in fall:
    print('fall')
else:
    print(f'error: {month} is invalid')

# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = 'banana'

if fruit in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(fruit)
    print(f'The new list of fruits is {fruits}')

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#  * Check if the person dictionary has skills key, if so print out the first skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'),
#  if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

keys= person.keys()

if 'skills' in keys:
    first_skill= person['skills'][0]
    print(first_skill)
    if 'Python' in person['skills']:
        print(f"Python: {'Python' in person['skills']}")
    else:
        print(f"Python: {'Python' in person['skills']}")
else:
    print('No skills key')

if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    if len(person['skills'])==2:
        print('He is exlusively a frontend developer')
    else:
        print('He has frontend developer skills')
else:
    print('No complete frontend skills')

if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    if len(person['skills'])==3:
        print('He is exlusively a backend developer')
    else:
        print('He has backend developer skills')
else:
    print('No complete backend skills')

if person['is_married']==True and person['country']=='Finland':
    print(f"{person['first_name']} lives in {person['country']}. He is married")



