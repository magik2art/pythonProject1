import csv


def read_something(path, start, finish):
    with open(path) as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 1
        # sum = "1000"
        # print(type(x))
        for row in file_reader:
            if count >= int(start) and count <= int(finish):
                print('Record number:', {count}, ' - Sum: ', {row[0]})
            count += 1
        print('All record in file:', {count}, 'string.')
