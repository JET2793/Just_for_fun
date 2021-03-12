#Script by JET 04-May-18
#Calculation of roots by bisection

text = input('Number? ')
number = float(text)  #Must be a real number
if number < 0.0:
    print('Number must be positive, stupid!')
    exit()
elif number < 1.0:
    lower = number
    upper = 1.0
else:
    lower = 1.0
    upper = number

text = input('Tolerance? ')
tolerance = float(text)  #Must be a positive number
if tolerance < 0.0:
    print('Tolerance must be positive, stupid!')
    exit()

uncertainty = upper - lower

a = input('Power? ')
power = int(a)  #Must be an integer

while uncertainty > tolerance :
    middle = (lower + upper)/2
    
    if middle**power < number:
        lower = middle
    else:
        upper = middle

    print(lower, upper)
    uncertainty = upper - lower
print('Finished!')
exit()
