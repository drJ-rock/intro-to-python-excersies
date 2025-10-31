my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
even_or_odd = []

for number in my_list:
    if number % 2 == 0:
        num_type = 'even'
    else:
        num_type = 'odd'
    
    even_or_odd.append(num_type)

print(even_or_odd)