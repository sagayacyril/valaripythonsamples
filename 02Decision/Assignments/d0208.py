# Programming Series - Python3.0
# Day02: 008

# Write a python program to find maximum between three numbers.
a,b,c = input("Enter three numbers : ").split()
a = int(a)
b = int(b)
c = int(c)

if a > b:
    if a > c:
        print("Maximum :", a)
    else:
        print("Maximum :", c)
else:
    if b > c:
        print("Maximum :", b)
    else:
        print("Maximum :", c)
