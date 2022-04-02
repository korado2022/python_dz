# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя yield
max_num = 15
odd_nums = (i for i in range(1, max_num + 1, 2))
for num in odd_nums:
    print(num)
