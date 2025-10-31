def factorial(number):
    index = 1
    product = 1
    while index <= number:
        product = index * product 
        index += 1
    return product 

print(factorial(4))

def factorial2(numb):
    prod = 1
    for each in range(1, numb+1):
        prod *= each
    return prod

print(factorial2(4))

