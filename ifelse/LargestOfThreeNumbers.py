class LargestOfThreeNumbers:

 number1 = int(input('Enter number 1 : '))
 number2 = int(input('Enter number 2 : '))
 number3 = int(input('Enter number 3 : '))
 print('Number entered are :',number1,number2,number3)

 if number1>number2 and number1>number3:
     print('number 1 is the largest')
 if number2>number1 and number2>number3:
     print('number 2 is the largest')
 if number3>number1 and number3>number1:
     print('number 3 is the largest')