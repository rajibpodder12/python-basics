#Immutability of string
#TypeError: 'str' object does not support item assignment

name = 'Sam'

#name[0] = 'P'
#String concatenation, + sign does not put space before concatenating
concatenate_string = 'P' + name

print('Hello',name,'How are you?')
print('Hello'+name+'How are you?')
print('Hello '+name+' How are you?')
print(concatenate_string)
#convert string into list, split() 
Name = 'Hello World'
name_list = Name.split()
print(f'{name_list}')
#print the same sting multiple times
print(Name*3)


