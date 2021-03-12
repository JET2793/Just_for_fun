#Code edited by JET 04-May-18
#Determination of Odd/Even numbers

text = input('Number? ')
number = int(text)

if number % 2 == 0:
    print('Even number')
else:
    print('Odd number')


text = input('Try Again? (Yes=1/No=0)')
number = int(text)

if number == 1:
    text = input('Number? ')
    number = int(text)

    if number % 2 == 0:
        print('Even number')
    else:
        print('Odd number')

    print('That was fun!')

else:
    print('OK. Goodbye!')
