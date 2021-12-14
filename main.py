print('Яма')

# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Программа получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
#
# Примечаение: вводите однозначное число.

height = int(input('Введите высоту: '))

for i in range(1, height + 1):
    # string = ' ' * (height - i) + '#' * (2 * i - 1)
    numbers_simple = ''
    numbers_revers = ''
    for j in range(i):
      numbers_revers += str(height - j)
    for k in range(height - i, height):
      numbers_simple += str(k + 1)
    string = str(numbers_revers) + '.' * 2 * (height - i) + str(numbers_simple)
    print(string)

