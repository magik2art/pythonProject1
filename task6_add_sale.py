import argparse
import csv


parser = argparse.ArgumentParser(description='Return cost of Valutue. Input string:')
parser.add_argument('indir', type=str, help='Input dir for videos')
args = parser.parse_args()
sale = [str(args.indir).split(" ")]
print(sale)

def csv_dict_writer(path, fieldnames, data):
    with open(path, "a") as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

path = "file/bakery.csv"
fieldnames = sale[0]
print("Output all list:")

my_list = []
for values in sale[1:]:
    inner_dict = dict(zip(fieldnames, values))
    my_list.append(inner_dict)

csv_dict_writer(path, fieldnames, my_list)
