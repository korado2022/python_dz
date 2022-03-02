duration = 400153
result = ''

if duration > 86400:
    result += f'{duration // 86400} дн '
    duration %= 86400

if duration in range(3600, 86400):
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
