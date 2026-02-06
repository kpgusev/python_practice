import os
from pathlib import Path
import datetime

file_name = f'{Path(__file__).parent}/data/txt_20260206_2b2f78.txt'
separator = '|'

def to_none(value):
    return None

def to_date(value):
    return datetime.date(int(value[0:4]), int(value[5:7]), int(value[8:10]))

def get_type(value):
    if value == 'null':
        return to_none
    if len(value) == 10 and value[0:4].isdigit() and value[4] == '-' and value[5:6].isdigit():
        return to_date
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        return int
    value = value.replace('.', '', 1)
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        return float
    return str


with open(file_name) as file:
    file_source = file.read()
    columns_count = len(file_source.split('\n')[0].split(separator))
    columns_types = [to_none for i in range(columns_count)]
    for row in file_source.split('\n')[1:]:
        value_arr = row.split(separator)
        for value_indx in range(len(value_arr)):
            value = value_arr[value_indx]
            if (columns_types[value_indx] == to_none):
                columns_types[value_indx] = get_type(value)
            print(f'{get_type(value)(value.replace('"', ''))}', end='\t')
        print()
    print(columns_types)