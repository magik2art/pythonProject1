import argparse
import task6_read_all
import task6_WhatRead


#это код который добавляет работу через терминал
parser = argparse.ArgumentParser(description='Return cost of Valutue. Input string:')
parser.add_argument('-min', type=str, default=0, help='provide an integer (default: 2)')
parser.add_argument('-max', type=str, default=9999, help='Input dir for videos')
args = parser.parse_args()


path = "file/bakery.csv"  # путь к файлу для записи
if args.min == 0 and args.max == 9999:
    print("Вывод всех записей:")
    task6_read_all.all(path)
else:
    print("Найдены следующие записи:")
    task6_WhatRead.read_something(path, args.min, args.max)
