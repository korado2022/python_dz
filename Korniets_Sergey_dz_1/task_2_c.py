numbers =[num ** 3 for num in range(1000) if num % 2 != 0]
sum_numbers = 0

for num in numbers:
    num += 17
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num = num // 10
    if sum_num % 7 == 0:
        sum_numbers += sum_num
print(sum_numbers)
