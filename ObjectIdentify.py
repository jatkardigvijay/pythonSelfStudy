a = 50
b = a
print(id(a))
print(id(b))
#re assign value of a now
a = 500
print(id(a))
print(id(b))