# Programming Series - Python3.0
# Day02: 007

# Write a python program to check whether a year is leap year or not.

# https://en.wikipedia.org/wiki/Leap_year
"""
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""
year = int(input("Enter the year : "))
if year % 4:
    print("No, It is not leap year")
elif year % 100:
    print("Yes, It is leap year")
elif year % 400:
    print("No, It is not leap year")
else:
    print("Yes, It is leap year")
