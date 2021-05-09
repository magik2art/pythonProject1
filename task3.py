import csv


users = open('file/users.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(users)
x_users = []
for row in reader:
    x_users.append(" ".join(row))
users.close()

hobby = open('file/hobby.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(hobby)
x_hobby = []
for row in reader:
    x_hobby.append(" ".join(row))
hobby.close()

x_dict = {u:h for u, h in zip(x_users, x_hobby)}
print(x_dict)