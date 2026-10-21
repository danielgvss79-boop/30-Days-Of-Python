# 💻 Exercises: Day 8
# Create an empty dictionary called dog
dog = dict()
# Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Sara', 'color':'golden','age':10}
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Jason',
    'last_name':'Haag',
    'age':45,
    'country':'USA',
    'city':'Orlando',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('SQL')
student['skills'].append('Java')
print(student['skills'])
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
del student['first_name']
student.pop('last_name')
print(student)
# Delete one of the dictionaries
del student
print(student)
