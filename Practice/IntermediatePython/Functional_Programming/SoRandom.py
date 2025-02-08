import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

# Capitalize
def capitalize_suffix(suffix):
    return suffix.capitalize()

capital_suffix = list(map(capitalize_suffix, suffixes))

# Generate 10 fantasy name using capitalize suffix
random_names = [create_fantasy_name(prefixes, capital_suffix) for i in range(10)]

# Filtered names
def fire_in_name(name):
    return "Fire" in name

def concatenate_names(name1, name2):
    return name1 + ", " + name2

# Do list thing
nameWithFire = list(filter(fire_in_name, random_names))
filteredName = reduce(concatenate_names, nameWithFire)

def display_name_info():
    for i in random_names:
        print(i)
    print("Name with fire: ", nameWithFire)
    print("Reduced name: ", filteredName)

display_name_info()
