import random

print('Ходит игрок: ')
 
list = [1, 2]
random_index = random.randint(0, len(list)-1)
print(list[random_index])
h = list[random_index]
k_list = [i for i in range(1, 28)]
count = 0
N = 117
 
while N > 0:
    n = int(input('Введите количество конфет, которое возьмете от 1 до 28: '))
    N = N - n
    print(f'Осталость {N} конфет')
    count += 1
    print(f'{count} ход')
    n_bot = random.randint(0, len(k_list)-1)
    print(f'Соперник взял {n_bot} конфет')
    N = N - n_bot
    print(f'Осталось {N} конфет')
    count += 1
    print(f'{count} ход')
    
for i in list:
    if count%2:
        print(f'Победил игрок {h}! Ура!')
    else:
        if h == 2:
            print('Победил 1 игрок!')
        else:
            print('Победил 2 игрок!')