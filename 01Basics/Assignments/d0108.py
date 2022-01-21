# Programming Series - Python3.0
# Day01: 008

# Write a python to convert Fahrenheit to Celsius 
# and vice versa
# C = ( 5 .0 / 9.0  ) *  ( F – 32 )
# F = ( 9.0  / 5.0  ) * C + 32

f = float(input("Enter fahrenheit  : "))
c = 5.0 / 9.0 * (f - 32)
print("Fahrenheit : {:.3f}, Celsius : {:.3f}".format(f,c))

c = float(input("Enter celsius  : "))
f = 9.0/5.0 * c + 32
print("Celsius : {:.3f},  Fahrenheit : {:.3f}".format(c,f))
