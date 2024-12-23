x = "hello"

#format method

print('{}, how are you??????   '.format(x))

#f' string method

print(f'{x}, how are you??????')

#Concatenation method

print(x+', how are you??????')

print()

#format() method also work with index position

print('The {2} {1} {0}.....'.format('fox','brown','quick'))

print('The {q} {b} {f}.....'.format(f='fox',b='brown',q='quick'))

#Float number formatting

result = 100 / 777 

print('The result is {}'.format(result))
print('The result is {r:1.2f}'.format(r=result))
print('The result is {0:1.2f}'.format(result))
print(f'The result is {result:1.2f}')

# % => string formating operator
print('The result is %.2f, %.5f' %(result,result))
