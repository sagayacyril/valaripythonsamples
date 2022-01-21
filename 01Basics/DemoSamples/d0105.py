# Bitwise demo
num1 = 9
num2 = 10
print(type(num1), type(num2))

# Demo AND 
result = num1 & num2
print("AND --> {} & {} = {} at {}".format(num1,num2,result,hex(id(result))))

# Demo OR 
result = num1 | num2
print("OR --> {} | {} = {} at {}".format(num1,num2,result,hex(id(result))))

# Demo XOR 
result = num1 ^ num2
print("XOR --> {} ^ {} = {} at {}".format(bin(num1),bin(num2),bin(result),hex(id(result))))

# Demo left Shift
num1 = 1
print("{} = {} << 1 {} at {}".format(num1, bin(num1),bin(num1),hex(id(num1))))
num1 = num1 << 1
print("{} = {} << 1 {} at {}".format(num1, bin(num1),bin(num1),hex(id(num1))))
num1 = num1 << 1
print("{} = {} << 1 {} at {}".format(num1, bin(num1),bin(num1),hex(id(num1))))
num1 = num1 << 1
print("{} = {} << 1 {} at {}".format(num1, bin(num1),bin(num1),hex(id(num1))))

# Demo right Shift
num1 = num1 >> 1
print("{} = {} >> 1 {} at {}".format(num1, bin(num1),bin(num1),hex(id(num1))))
num1 = num1 >> 1
print("{} = {} >> 1 {} at {}".format(num1, bin(num1),bin(num1),hex(id(num1))))
num1 = num1 >> 1
print("{} = {} >> 1 {} at {}".format(num1, bin(num1),bin(num1),hex(id(num1))))
num1 = num1 >> 1
print("{} = {} >> 1 {} at {}".format(num1, bin(num1),bin(num1),hex(id(num1))))