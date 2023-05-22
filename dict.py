'''Создание словаря'''
super_dict = {'name': 'Брюс', 'hero': 'Бэтмен', 'city': 'Готэм', 'age': 30}
print(super_dict)


'''Вывод элемента словаря'''
print(super_dict['name'])
# Вывод: Брюс


'''
Вывод элемента словаря с помощью метода .get()
Если ключа в словаря нет, то не возвращает ошибку, 
а пишет второй аргумент ("Засекречено" в данном случае)
'''
print(super_dict.get('hobby', 'Засекречено'))
# Вывод: "Засекречено"

print(super_dict.get('city', 'Засекречено'))
# Вывод: "Готэм"


'''Добавление и изменение элементов'''
super_dict['drink'] = 'Кофе'  # добавление новых ключ + значение
super_dict['city'] = 'Челябинск'  # изменение существующего значения
print(super_dict)
# Вывод: {'name': 'Брюс', 'hero': 'Бэтмен', 'city': 'Челябинск', 'age': 30, 'drink': 'Кофе'}


'''Удаление из словаря'''
del super_dict['name']  # удаление
print(super_dict)
# Вывод: {'hero': 'Бэтмен', 'city': 'Челябинск', 'age': 30, 'drink': 'Кофе'}


'''Итерация по словарю'''
for key, value in super_dict.items():
    print(f"Ключ: {key}, Значение: {value}")



'''РАЗБОР МЕТОДОВ СЛОВАРЯ'''

'''.keys() -> получение ключей словаря'''
print(super_dict.keys())
# Вывод: dict_keys(['hero', 'city', 'age', 'drink'])

# Из-за неудобности работы с dict_keys, предлагаю сразу делать преобразование в список
my_list = list(super_dict.keys())
print(my_list)
# Вывод: ['hero', 'city', 'age', 'drink']

# Либо, если нам нужны ключи только для дальнейшего итерирования
for key in super_dict.keys():
    print(key)


'''.values() -> получение значений словаря'''
print(super_dict.values())
# Вывод: dict_values(['Бэтмен', 'Челябинск', 30, 'Кофе'])

# Из-за неудобности работы с dict_values, предлагаю сразу делать преобразование в список
my_list = list(super_dict.values())
print(my_list)
# Вывод: ['Бэтмен', 'Челябинск', 30, 'Кофе']

# Либо, если нам нужны значения только для дальнейшего итерирования
for val in super_dict.values():
    print(val)


'''.items() -> получение пары ключ + значение'''
print(super_dict.items())
# Вывод: dict_items([('hero', 'Бэтмен'), ('city', 'Челябинск'), ('age', 30), ('drink', 'Кофе')])

# Из-за неудобности работы с dict_items, предлагаю сразу делать преобразование в список
my_list = list(super_dict.items())
print(my_list)
# Вывод: [('hero', 'Бэтмен'), ('city', 'Челябинск'), ('age', 30), ('drink', 'Кофе')]

# Либо сразу использовать для итерирования
for key, value in super_dict.items():
    print(f"Ключ: {key}, Значение: {value}")


'''.pop() -> удаляет пару "ключ-значение" по ключу и возвращает ее значение'''
removed_value = super_dict.pop('age', None)
print(removed_value) # значение, которое было удалено
# Вывод: 30

print(super_dict) # Обновленный словарь без age
# Вывод: {'hero': 'Бэтмен', 'city': 'Челябинск', 'drink': 'Кофе'}


'''.update() -> объединение словарей'''
new_params_dict = {'city':'Готэм', 'friend':'Робин'} # это словарь с новыми параметрами
super_dict.update(new_params_dict) # делаем апдейт
print(super_dict)
# Вывод: {'hero': 'Бэтмен', 'city': 'Готэм', 'drink': 'Кофе', 'friend': 'Робин'}

'''.clear() -> очистка словаря'''
super_dict.clear()
print(super_dict)  # выводит: {}