def func_1(*args):
    print(type(args))
    print(args)
    return sum(args)
print(func_1(1,2,3,4,5,6,7,8,9,10))

def func_2(**kwargs):
    print('\n')
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f'\n{key} => {value}\n')
func_2(name="rajib",surname="podder")
