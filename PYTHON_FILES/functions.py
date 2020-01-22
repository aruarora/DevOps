# Some Builtin Functions
"""
print dir(1)
str1 = "Welcome to Functions."
print len(str1)
print range(len(str1))

print type(range(len(str1)))
"""
# Function Syntax
'''
def function_name("arg1", "arg2"):
    code
    return "value"
'''

def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(23,45)
print out

def add(arg1, arg2):
    return arg1 + arg2

out = add(4,5)

print out


def print_msg(var1):
    print "Hello, Good " + var1
    return "Welcome."

# print_msg("Night")

print print_msg("Evening")
# print_msg("Morning")







