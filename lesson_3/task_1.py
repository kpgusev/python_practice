import os
from pathlib import Path
import pprint


data_dir = f'{Path(__file__).parent}/data'
frames = []

for f in os.listdir(data_dir):
    if Path(f).suffix == 'dat':
        frames.append(f'{data_dir}/{f}')

data = []

for i in frames:
    with open(i) as f:
        data.append(list(map(float, f.readlines())))

def custom_operator(l, arr):
    m = arr[0]
    for i in arr:
        if l(i, m):
            m = i
    return m

def custom_min(arr):
    return custom_operator(lambda x, y: x < y, arr)

def custom_max(arr):
    return custom_operator(lambda x, y: x > y, arr)

def custom_avr(arr):
    s = 0
    for i in arr:
        s += i
    return s / len(arr)

def custon_med(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        return arr[len(arr) // 2 + 1]
      
        
slovar = []
for i in range(len(data)):
    d = data[i]
    q = {
        'name': frames[i],
        'min': custom_min(d),
        'max': custom_max(d),
        'avr': custom_avr(d),
        'med': custon_med(d),
    }
    slovar.append(q)
    with open(f'{data_dir}/{Path(frames[i]).stem}.output', 'w') as f:
        f.write(str(q))
