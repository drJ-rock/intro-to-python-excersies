my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0

while index < len(my_list):
    index1 = 0
    while index1 < len(my_list[index]):
        number = my_list[index][index1]
        if number % 2 == 0:
            print(number)
        
        index1 += 1
    
    index += 1
    
    
        



    