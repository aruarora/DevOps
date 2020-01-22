x = 2
y = 3
total = x + y
print total

# Comparison Operators

a = 21
b = 51

out = a < b
print out

out = a > b
print out

out = a == b
print out

out = a != b
print out

out = (a <= b)
print out

out = (a >= b)
print out

# Logical Operators, and/or

a= 10
b= 20

output = (a <= b) or (a >= b)
print "Logical operators"
print output

output = (a <= b) or (a != b)
print output

output = (a <= b) and (a != b)
print output

output = (a <= b) and (a >= b)
print output

output = not(a <= b)
print output

output = not((a <= b) and (a >= b))
print output


# Membership Operator/ Tests for member in a sequences such as string, lists or tuples.

devops = ["Jenkins", "Ansible", "AWS", "Swarn", "Kubernestes"]
print devops

ans = "AWS" in devops
nans = "Azure" not in devops

print ans
print nans


skill = "devops"

x = "d" in skill
print x













