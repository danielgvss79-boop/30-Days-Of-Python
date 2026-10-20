# 💻 Exercises: Day 6

# Exercises: Level 1
# Create an empty tuple
tuple = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Mate','Danny')
siblings = ('Sara','Sole')
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + siblings
print(siblings)
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Sandra', 'Orlando')
family = parents + siblings
print(family)

# Exercises: Level 2
# Unpack siblings and parents from family_members
list(family)
parents = family[0:2]
siblings = family[2:]
print(parents)
print(siblings)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple','coconut','banana')
vegetables = ('carrot','lettuce')
animal_p = ('beef','chicken','fish')
food_stuff_tp = fruits + vegetables + animal_p
# Change the about food_stuff_tp tuple to a food_stuff_lt list
list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print('lettuce' in food_stuff_tp)
print(food_stuff_tp[4])
# Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_tp)
print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])
# Delete the food_stuff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
# food_stuff_tp[0]
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)

