my_dict = {'Denis': 111111, 'Anton': 222222, 'Ivan': 333333, 'Alexander': 444444, 'Yaroslav': 555555, 'Vladimir': 666666, 'Yury': 777777}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Sanya', 'Sanyi net, zato yest Alexander'))
my_dict.update({'Leonid': 888888, 'Maksim': 999999})
fired = my_dict.pop('Denis')
print(fired)
print(my_dict)

my_set = {1, 2, 2, 2, 2, 3, 4, 5, 'word', 'number', 'number', (1, 2, 3), 2.2, 2.2}
print(my_set)
my_set.update({'cat', 'dog'})
my_set.remove('word')
print(my_set)
