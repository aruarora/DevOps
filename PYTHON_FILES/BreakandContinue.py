My_Country = {"Country": "India", "Flag": "Tricolor", "Currency": "Rupees", "DOI":"15thAug", "Independence_Year": 1947, "TimeOfFreedom": 2300}

# print My_Country
"""
# By default keys are assumed from the dictionary
for I in My_Country:
    print I
    
# By dict.keys() will return LIST of keys

for I in My_Country.keys():
    print "dict.keys()"
    print I

# By dict.values() will return LIST of values
for I in My_Country.values():
    print "dict.values()"
    print I
"""

# Break Statement

PLANETS = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
'''
for planet in PLANETS:
    print "I am going over planet: ", planet
    if planet == "Mars":
        print "Landing on planet ", planet
        break

print "Out of for loop."

# Continue Statement


for planet in PLANETS:
    if planet == "Jupiter":
        print "Skipping this planet", planet
        continue
    print "I am landing on planet: ", planet


print "Out of for loop."
'''
# Break statement in while loop

x = 0

while True:
    print "Value of x is: ", x
    x = x + 1
    if x == 5:
        print "Breaking the loop as x is: ", x
        break

print "Out of while loop"


# Continue/Break statement in for loop

for i in "Python":
    if i == "t":
        continue
    print "Value of i is", i


print "Out of for loop"





