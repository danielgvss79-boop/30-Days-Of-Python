# 💻 Exercises - Day 4
# Declare a variable named company and assign it to an initial value "Coding For All".
company = "coding for all"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
company = company.upper()
print(company)
# Change all the characters to lowercase letters using lower() method.
company_l = company.lower()
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
c = company[:6]
print(c)
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("CODING"))
# Replace the word coding in the string 'Coding For All' to Python.
company = company.replace("CODING","PYTHON")
print(company.lower())
# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
splat = companies.split(',')
print(splat)
# What is the character at index 0 in the string Coding For All.
first = company[0]
print(first)
# What is the last index of the string Coding For All.
print(company[-1])
# What character is at index 10 in "Coding For All" string.
print(company[9])
# Use index to determine the position of the first occurrence of C in Coding For All.
placer = 'placer'
print(placer.index('p'))
