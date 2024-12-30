def square(num):
    return num ** 2
print(square(2))

# lambda function equivalent
# anonymous function
# def square(num) = replace with lambda
square = lambda num: num ** 2
print(square(5))
print(list(map(lambda num: num ** 2,[1,2,3,4,5,6,7,8,9,10])))
