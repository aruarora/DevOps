# Understanding Type Casting, print formats & User Input

x = 21
y = "STAR"
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")

inputstr = raw_input("Enter any string: ")
print type(inputstr)

inputINT = input("Enter a number: ")
print type(inputINT)

'''
print y
print "The value of y is ", y
print "The value of y is" + " " + y
print "My code number is " + " " + str(31)

print "%s is the value of y" % y
print "%d is the value of x" % x

print "%s is the value of y and %d is the value of x"  % (y,x)
print "%s is the value of y and %s is the value of x"  % (y,x)

print "%s is the value of Development" % list(Development)
'''
"""
print type(x)
print type(y)
print type(Development)

x = str(x)

print "After type casting x is converted to a STRING."
print type(x)

Development = list(Development)
print "After type casting Development is converted to a LIST."
print type(Development)

"""

