number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

print(f'Before swapping: number1 => {number1} and number2 => {number2}')

number1, number2 = number2, number1

print(f'After swapping: number1 => {number1} and number2 => {number2}')