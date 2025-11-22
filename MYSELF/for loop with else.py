softwares = ['Python', 'Office', 'Avro', 'Git', 'Pycharm', 'Aanaconda', 'Panda']

for soft in softwares:
    print(soft)
    if soft == 'Panda':
        break
else:
    print('Nothing is installed')

s = 0
while s < len(softwares):
    print(f'While = Installed software: {softwares[s]}')
    s += 1
