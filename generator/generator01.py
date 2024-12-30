def create_cubes(n):
    # result = []
    for x in range(n):
        # result.append(x ** 3)
        yield x ** 3
    # return result

print(list(create_cubes(10)))

def fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b=b,a+b

for i in fibonacci(10):
    print(i)

print(list(fibonacci(10)))

def gen_simple():
    for i in range(3):
        yield i
g = gen_simple()
print(next(g))
print(next(g))