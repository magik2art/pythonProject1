import csv

def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    i = 0
    for row in reader:
        i += 1
        print(' '.join(row))


def all(read_path):
    with open(read_path, "r") as f_obj:
        csv_reader(f_obj)
