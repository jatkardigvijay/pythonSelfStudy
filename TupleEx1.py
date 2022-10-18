tup = ('hi', 'python', 2)
#checking type
print(type(tup))

#print the tuple
print(tup)

#tuple slicing
print(tup[1:])
print(tup[0:1])

#tuple concatenation using + operator
print(tup + tup)

#tuple repition using * operator
print(tup*3)

#tuple add value(throws an error). we cannot add values to tuple
tuple[4] = 'Hello'
print(tup)