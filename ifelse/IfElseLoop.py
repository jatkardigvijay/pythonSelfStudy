class IfElseLoop:
    number = int(input('Enter a nunber : '))

    if number > 100:
        print('Number is greater than 100, Please enter the number again')
    elif 85 <= number <= 100:
        print('Grade A')
    elif 71 <= number < 85:
        print('Grade B')
    elif 56 <= number <= 70:
        print('Grade C')
    elif 40 <= number < 55:
        print('Grade D')
    else:
        print('You have failed')
