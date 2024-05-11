

with open('datalog.txt', 'w') as f:
    data = []
    for rx in range(0, 180, 5):
        for rz in range(0, 180, 5):
            f.write(f'{rx} {rz} 100\n')
    print(data)
    