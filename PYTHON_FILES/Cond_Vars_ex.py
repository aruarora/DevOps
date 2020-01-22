
""" This script will implement our knowledge on
conditions and different datatypes."""

print "This IT Organization has various skill sets."
print "Find out your match."

print "Enter Capitalised Values: "

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "Code":1218}


usr_skill = raw_input("Enter your desired skill: ")



# Check with conditions if we have this skill in List, Tuple, Dict.keys()
if (usr_skill in DevOps):
    print "We have this skill in DevOps Team."
elif (usr_skill in Development):
    print "We have this skill in Development Team."
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print "We have contract employess with this skill."
else:
    print "Skill not found."
    print "Please check if you have entered value in capitalize or check the spelling."