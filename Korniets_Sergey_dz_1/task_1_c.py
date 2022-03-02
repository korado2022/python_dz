duration = 4153
result = ''

if duration > 3600:
    result += f'{duration // 3600} час '
    duration %= 3600
else:
    result += '0 час '

if duration in range(60, 3600):
    result += f'{duration // 60} мин '
    duration %= 60
else:
    result += '0 мин '

if duration in range(60):
    result += f'{duration} сек'

print(result)
