immutable_var = 1, 1.5, 'word', False, [10, 20, 30]
print(immutable_var)
# immutable_var[2] = 'number'   # tuples can't be changed.
immutable_var[4][0] = -10   # PyCharm allows to change only list data in a tuple
print(immutable_var)
mutable_list = [1, 1.5, 'word', False, 10, 20, 30]
mutable_list[2] = 'number'.upper()
mutable_list[3] = True
mutable_list[4] = -10
mutable_list.append(40)
mutable_list.remove(20)
print(mutable_list)
