#find all odd numbers

x = [ i for i in range(1,11) if i % 2 == 1]
print(x)

y = [ j*i for i in range(1,11) for j in range(1,11) ]

print(y)