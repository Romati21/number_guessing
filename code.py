from random import randint

left, right = 1, 1000
middle = (left + right) // 2
count = 0
num = randint(left, right)
while middle != num:
    if middle > num:
        right = middle - 1
        middle = (left + right) // 2
        count += 1
    elif middle < num:
        left = middle + 1
        middle = (left + right) // 2
        count += 1
print(f'Количество попыток: {count}, это число: {middle}')
