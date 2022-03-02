duration = 153
result = ''

if duration > 60:
    result += f'{duration // 60} мин '
    duration %= 60
else:
    result += '0 мин '

if duration in range(60):
    result += f'{duration} сек'

print(result)
