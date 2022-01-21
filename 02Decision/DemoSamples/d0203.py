# Programming Series - Python3.0
# Day02: 003

# Write python program to check is the given name is short or long
# If name has characters < 7 then let us consider it as short one
# otherwise not.

name = input("Enter Name : ")
namelen = len(name)
if namelen < 7:
    print(name, "is the short name")
else:
    print(name, "is the long name")
