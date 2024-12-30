def func():
    while True:
        try:
            result = int(input("Please provide number:"))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Thank you!!!")
            break;
        finally:
            print("End of try/except/finally")

func()

