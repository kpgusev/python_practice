import os
from pathlib import Path
import datetime
import json


class Column:
    def __init__(self, title, units):
        self.title = title
        self.units = units
    
    def __repr__(self):
        return f'{self.title} in {self.units}'

file_name = f'{Path(__file__).parent}/data/PR25.IB051630_11.txt'
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

data = {
    'columns': [],
    'data': []
}

with open(file_name, errors='replace') as file:
    lines = 0
    row = file.readline()
    while row:
        if 'Lines' in row:
            lines = int(row.replace(' ', '')[6:])
            break
        row = file.readline()
    file.readline()
    titles_data = file.readline()
    titles = []
    units_data = file.readline()
    units = []
    for i in titles_data[10:].replace('\n', '').split(' '):
        if i != '':
            titles.append(i)
            data['data'].append([])
    for i in units_data[2:].replace(']', '').replace('[', '').replace('\n', '').split(' '):
        if i != '':
            units.append(i)
    columns_count = len(titles)
    data['columns'] = [Column(titles[i], units[i]) for i in range(len(titles))]
    data['columns'].append(Column('Dataset', 'index'))
    data['data'].append([])

    file.readline()
    for i in range(lines - 100):
        row = file.readline().replace('\n', '')
        fine_row = ''
        ls = ' '
        for i in row:
            if i != ' ':
                fine_row = fine_row + i
                ls = i
                continue
            if ls != ' ':
                fine_row = fine_row + ';'
            ls = i
        for i in range(len(fine_row.split(';'))):
            data['data'][i].append(get_type(fine_row.split(';')[i])(fine_row.split(';')[i]))

print(data)