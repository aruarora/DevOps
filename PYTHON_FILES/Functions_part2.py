# Keyword Argument
"""
def print_info(name, age):
    print "Welcome User: ", name
    print age
    if (age > 50) and (age <= 75):
        print "You seem to be very experienced Individual."
    elif (age > 75) and (age <=100):
        print "You can teach your experience to the experienced Individuals."
    elif age > 100:
        print "Hope you live more and record your name in guinness world record."
    else:
        print "Lot of milestone to cover yet. All the best."

print_info("Imran", 105)
print_info(age=80, name="Imran")
"""

# Default Argument
"""
def order(food="Salad"):
    print "Your order %s is placed and will be delivered to you in 30 Mins" % food

order()
order("Wrap")
"""

# Variable Lenght Argument

def order_food(min_order, *foods):
    print "Your have ordered: ", min_order
    print type(foods)
    for item in foods:
       print "You have ordered: ", item
    print "Your food will be delivered in 30 mins. "

order_food("Salad", "Sandwich", "Soup", "Noodles", "Smoothie", "Ice Cream")









