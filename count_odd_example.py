#add the odd numbers between 0 and 5000

#setup
result = 0
num = 0

#work!
#lets look at the numbers 0-5000
while num <= 5000:
    is_odd = num % 2 != 0
    if is_odd:
        print(num)
        result += num
    num += 1



#return result
print(result)