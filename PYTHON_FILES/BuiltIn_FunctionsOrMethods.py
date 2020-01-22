# String Built in methods/functions
message = "hello & welcome to built in methods of python."

# Capitalizing string
print message
message = message.capitalize()

print message

# Find a substring in String

print message.find("welcome")
print message.find("java")
print message.find("python", 20)
print message[39:45]
# print message.find("Hello", 10)

# join a sequence into a string
seq = ("192", "168", "1", "10")
print ".".join(seq)
print "-".join(seq)
print "/".join(seq)

# strip whitespaces from the end of the string.
a = "Hello                     "
b = "Folks"
print a + " " + b
print a.strip() + " " + b

# split: Splits string acording to delimeter str(space if not provided), return list of substring.
str1 = "Python is very interesting."

print str1.split()

# is methods in string: Return true or false
str2 = "Python"
str3 = "Python2"

#print str2.isalpha()
#print str3.isalnum()

# dir() function will return list of Available methods in String, List, Tuple or dictionary datatype
# print dir("")
#print dir([])
#print dir(())
# print dir({})

# .append method of List

Development = ["Nodejs", "Angularjs", "Java", ".net", "Python"]
print Development
Development.append("PHP")

print Development

# .extend method of List

devops=["Jenkins", "Ansible", "Docker", "Terraform", "Vagrant"]
print devops
print devops.extend(Development)

print devops


# .insert: Insert a element into the specified index value

devops=["Jenkins", "Ansible", "Docker", "Terraform", "Vagrant"]

devops.insert(3,"Scripting")
print devops


# .pop: Remove element from a list at a specified index value. default is last index

print devops
devops.pop()
print devops

devops.pop()
print devops

devops.pop()
print devops

devops.pop(1)
print devops


# Dictionary Built in

My_Country = {"Country": "India", "Flag": "Tricolor", "Currency": "Rupees", "DOI":"15thAug", "Independence_Year": 1947, "TimeOfFreedom": 2300}

print My_Country.keys()
print My_Country.values()
print My_Country.has_key("Flag")
print My_Country.














