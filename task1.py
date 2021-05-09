import requests
import re


# этот код сохраняет файл с логом
r = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
# params=payload)
r_json = r.text
print(type(r_json))
file_1 = open('file/hello.txt', 'w', encoding='utf-8')
content = file_1.writelines(r_json)
file_1.close()

# этот код парсит и записывает в cort все 3 типа по дз
cort = []
file_1 = open('file/hello.txt', 'r', encoding='utf-8')
for line in file_1:
    text = line.strip()
    remote_addr = re.sub(r'- -.*$', "", text)
    request_type = re.sub(r' /.*$', "", text)[::-1]
    request_type = re.sub(r'".*$', "", request_type)[::-1]
    requested_resource = re.sub(r'" .*$', "", text)[::-1]
    requested_resource = "/" + re.sub(r'/ .*$', "", requested_resource)[::-1]
    cort.append(([remote_addr] + [request_type] +[requested_resource]))
print(cort)
file_1.close()