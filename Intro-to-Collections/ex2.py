stuff = ('hello', 'world', 'bye', 'now')

stuff_list = list(stuff)

print(stuff_list)

stuff_list[2] = 'goodbye'

print(stuff_list)

stuff = tuple(stuff_list)

print(stuff)