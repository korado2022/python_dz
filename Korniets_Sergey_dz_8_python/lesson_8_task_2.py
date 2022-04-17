# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
# урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# ) для получения информации вида: (<remote_addr>, <request_datetime>,
# <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
# /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
# '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
# (^(?:\d{1,3}\.){3}\d{1,3})\s-\s-\s\[\d{1,2}/\w{3,9}/\d{4}(?::\d{2}){3}\s\+\d{4}\]\s\"[A-Z]{3}\s/\w{9}/\w{7}_\d\s[A-Z]{4}/\d\.\d\"\s\d{3}\s\d{1,4}

# Вариант для одной строки

import re
raw = '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'
parsed_raw = []
pars = ('(^(?:\d{1,3}\.){3}\d{1,3})', '\d{1,2}/\w{3,9}/\d{4}(?::\d{2}){3}\s\+\d{4}', '(?<=\s\")[A-Z]{3,4}', '/[a-z]{9}/[a-z]{7}\_\d', '(?<=\d\"\s)\d{3}', '\d{1,3}(?=\s\")')

for par in pars:
    parsed_raw.extend(re.findall(par, raw))

print(tuple(parsed_raw))

# Вариант для файла
with open('parsed.txt', 'a+', encoding='utf-8') as f_pars:
    with open('nginx_logs.txt') as f_nginx:
        for line in f_nginx:
            res = []
            for par in pars:
                res.extend(re.findall(par, line))
            f_pars.write(', '.join(res) + '\n')
