def func(number):
    try:
        return number % 0
    #there could be multiple except block
    except ZeroDivisionError:
        print("Number can not divided by zero!!!!")
    finally:
        print("We can not devide the any number by zero!!!!")

func(100)