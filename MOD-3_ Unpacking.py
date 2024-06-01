
# Домашнее задание по уроку "Распаковка параметров и параметры функции"



# 1.Функция с параметрами по умолчанию:

print('"Функция с параметрами по умолчанию"')

def print_params(a=1, b='строка', c=True):
    print(f'Значение a: {a}')
    print(f'Значение b: {b}')
    print(f'Значение c: {c}')

print(f'   Первый вызов:')
print_params()
print(f'   Второй вызов:')
print_params(42)
print(f'   Третий вызов:')
print_params(b=25)
print(f'   Четвертый вызов:')
print_params(c=[1, 2, 3])
print()
print()





#2.Распаковка параметров:

print('"Распаковка параметров"')

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_list = [500, 'Programm', True]
values_dict = {'a': 25, 'b': 'Anna', 'c': None}

print_params(*values_list)
print_params(**values_dict)
print()
print()





# 3.Распаковка + отдельные параметры:

print('"Распаковка + отдельные параметры"')

def print_params(a=10, b='Txt', c=True):
    print(a, b, c)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print()
print()





