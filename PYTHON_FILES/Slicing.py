# Indexed Datatypes
# String, List, Tuple

str1 = "This is a string."

# Positive Index values
print str1[0]
print str1[1]
print str1[2]
print str1[3]

# Negative Index Values
print str1[-1]
print str1[-2]


# Extracting Sub string / Slicing
print str1[0:4]
print str1[-7:-1]

# Slicing again
MSG="Hello and Welcome to Python Slicing"
print MSG[10:17]
msg1 = MSG[10:17]

print msg1


# Default Index range
print MSG[0:]
print MSG[:]

print MSG[:6]

# Slicing List
devops=["Jenkins", "Ansible", "Docker", "Terraform", "Vagrant"]

print devops[0]
print devops[1:4]
print devops[1:4][1]
print type(devops[1:4][1])
print devops[1:4][1][0:4]
print devops[1:4][1][0:4][-1]

# Slicing Tuple
devops=("Jenkins", "Ansible", "Docker", "Terraform", "Vagrant")

print devops[0]
print devops[1:4]
print devops[1:4][1]
print type(devops[1:4][1])
print devops[1:4][1][0:4]
print devops[1:4][1][0:4][-1]

# Dictionary Example
Skills = {"devops":("Jenkins", "Ansible", "Docker", "Terraform", "Vagrant"), "Developement": ["Java", ".net", "nodejs", "Angularjs"]}
print Skills["devops"]
print Skills["devops"][3]