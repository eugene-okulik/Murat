#Cоздал словарь my_dict
my_dict = {'tuple': (None, False, 1, 3, 'tuple_text', 58.6),
           'list': [1, 2, 3, 'list_text', 98.35, True],
           'dict': {'integer' : 4, 'boolean' : True, 'float' : 6.3, 6 : 'six', 'dict_text' : 'dict_text'},
           'set': {6, 'blabla', None, 8, 'set_text', 4.5}}

#Вывел последний элемент tuple
print(my_dict['tuple'][-1])

#Добавил в конец списка элемент и удалил 2 элемент
my_dict['list'].append(45)
my_dict['list'].pop(1)

#Добавил в dict элемент с ключом 'i am a tuple' и удалил люой элемент
my_dict['dict'] ['i am a tuple'] = 15
my_dict['dict'].pop('boolean')

#Добавил в set новый элемент и удалил элемент
my_dict['set'].add('new_text')
my_dict['set'].discard(4.5)

#Ввыводим на экран словарь
print(my_dict)