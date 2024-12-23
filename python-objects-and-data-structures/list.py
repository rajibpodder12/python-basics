#list is ordered sequence of elements
my_list = [1,2,3]
mixed_list = ['string',10.23,3]
print(f'the length of {my_list} of {len(my_list)}.')
print(f'the length of {mixed_list} of {len(mixed_list)}.')
#List concatenation
new_list = my_list+mixed_list
print(new_list)
#reversing using Slicing  and indexing example
print(my_list[::-1])
print(my_list[1])

#List mutating
print(my_list)
my_list[0]=5
print(my_list)

my_list.append(10)
print(my_list)

my_list.pop(1) # pop() method remove last item from the list 
print(my_list)

my_list.insert(1,2)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)