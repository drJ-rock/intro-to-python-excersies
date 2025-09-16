def multiply(left, right): # mulitply, left, right
    return left * right # left, right

def get_num(prompt): # get_num
    return float(input(prompt)) # prompt

first_number = get_num('Enter the first number: ') #get_num, first_number
second_number = get_num('Enter the second number: ') #get_num, second_number
product = multiply(first_number, second_number) # product
print(f'{first_number} * {second_number} = {product}')

#global: first_number, second_number, get_num, product, multiply
#built-in: print, float, input
#local: left, right, prompt

#function names: line 1, multiply; line 4 get_num; line 5 float, input
# line 10 print

#parameters: line 1 left, right; line 4 prompt