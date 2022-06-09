numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# List Comprehension 1
squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)

# List Comprehension 2
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# List Comprehension 3

with open("file1.txt") as file_1:
    list_1 = file_1.readlines()

with open ("file2.txt") as file_2:
    list_2 = file_2.readlines()

result = [int(number) for number in list_1 if number in list_2]

print(result)