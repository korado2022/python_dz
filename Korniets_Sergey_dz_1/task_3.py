for per in range(1, 101):
    if 4 < per < 21 or 4 < per % 10 <= 9 or per % 10 == 0:
        print(f'{per} процентов')
    elif per == 1 or per % 10 == 1:
        print(f'{per} процент')
    elif 1 < per < 5 or 1 < per % 10 < 5:
        print(f'{per} процента')
