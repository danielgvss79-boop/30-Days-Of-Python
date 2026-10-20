# 💻 Exercises: Day 7
# # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Placer.ai','Rappi'])
print(len(it_companies))
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print(len(it_companies))
# What is the difference between remove and discard


# Exercises: Level 2
# Join A and B
C = A.union(B)
print(C)
# Find A intersection B
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Delete the sets completely
del A
del B
del C
# print(A.symmetric_difference(B))

# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(f'list is {len(age)}')
age2 = set(age)
print(f'list is {len(age2)}')
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?'
sentence = sentence.split()
letters = set()
for word in sentence:
    set(word)
    letters = letters.union(word)
print(letters)
print(len(letters))
