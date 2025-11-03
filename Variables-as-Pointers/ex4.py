dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])   # [1, 42, 3] - it will be same as printing dict1 b/c it's a nested list that is stored in the same place