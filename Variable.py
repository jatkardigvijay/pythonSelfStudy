#declare variable and initalize it
x = 101

#global variable in function
def mainFunction():

    #printing a global variable
    global x
    print(x)

    #modifying a global variable
    x = 'Welcome to Ireland'
    print(x)

mainFunction()
print(x)