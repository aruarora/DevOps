#!/usr/bin/python

import os

userlist =['alpha1','beta1','gamma1']

for users in userlist:
  print (("Users in the userlist are %s") %users)
  exitcode = os.system(("id %s") %users)
  if (exitcode != 0):
    print("Add user %s to the group" %users)
    os.system(("useradd %s") %users)
    print (("user %s added") %users)
  else:
    print(("user %s already exist") %users)

exitcodegrp = os.system("grep science /etc/group")
if (exitcodegrp != 0):
  print ("Adding group")
  os.system("groupadd science")
else:
  print("group qlready exist")



for users in userlist:
  print("adding users to group science")
  os.system(("usermod -G science %s") %users)


dirpath = os.path.isdir("/opt/science_dir")
if (dirpath):
  print("directory path /opt/science_dir already exist")
else:
  os.mkdir("/opt/science_dir")


print ("provide ownership of science group to directory and add permissions")

os.system("chown :science /opt/science_dir")
os.system("chmod 770 /opt/science_dir")
