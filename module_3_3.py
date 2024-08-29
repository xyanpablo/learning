def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [0.1234, [5, 6, 7, 8, 9], 'string']
values_dict = {'a': False, 'b': [5, 6, 7, 8, 9], 'c': 'string'}
values_list_2 = [54.32, 'Строка']
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
