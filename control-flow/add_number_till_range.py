number = int(input('Enter the number till which you want to the sum:'))
sum = 0
for i in range(1,number+1):
    sum += i
else:
    print("End of for loop......")
print(f'Sum of the all numbers till {number} => {sum}')

# x = [sum for i in range(1,number+1) sum=sum+i]
# print(x)