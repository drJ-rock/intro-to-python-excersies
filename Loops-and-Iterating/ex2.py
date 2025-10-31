age = int(input('How old are you? '))
future_ages = []
for future_age in range(1,5):
    age += 10
    future_ages.append(age)
print(future_ages)
