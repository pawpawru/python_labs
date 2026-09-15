N = int(input('in_1: '))
data = []
for i in range(2, N+2):
    data += [input(f'in_{i}: ')]
    if not data[-1].strip():
        data = data[:-1]
        break
parts = []
for i in data:
    parts += [i.split()]
for i in parts:
    i[2] = int(i[2])
    i[3] = str(i[3])
data_2 = []
for i in parts:
    data_2 += [i[-1]]
offline = len([i for i in data_2 if i == 'True'])
online = len([i for i in data_2 if i == 'False'])
print(f'out: {offline} {online}')