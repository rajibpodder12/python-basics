#tuples are immutable
#tuples are within ()
#index() and count() method

t = (10,'hello',10)
print(t[0])
print(t.count(10)) #tuple count method returns the number of occurences of
                # particular element
print(t.index(10)) #index position of particular element.

# t[0] = 11 #'tuple' object does not support item assignment