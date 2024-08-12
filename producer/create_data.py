from random import randint

with open("data-bloom.txt", 'w') as f:
    for i in range(100):
        f.write(f'{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}\n')

