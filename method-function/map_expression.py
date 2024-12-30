#map bulit in function iterate over a 
#function over iteratable objects like list

def func(num):
    return num*num

my_list = [1,2,3,4,5,6,7,8,9,10]
for item in map(func,my_list):
    print(item)
# shortcut
print(list(map(func,my_list)))


