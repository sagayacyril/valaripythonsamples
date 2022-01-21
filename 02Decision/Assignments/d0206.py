# Programming Series - Python3.0
# Day02: 006

# Write a python program to check whether a number is divisible
# by 5 and 11 or not.

num = int(input("Enter number: "))
if (num % 5) and (num % 11):
    print("No, {} is not divisible by 5 & 11 without reminder".format(num))
else:
    print("Yes, {} is divisible by 5 & 11 without reminder".format(num))
