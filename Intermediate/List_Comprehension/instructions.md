# Instructions

## List Comprehension 1

You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

e.g. `4 * 4 = 16`
4 squared equals 16.
DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

Example Output
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

Make sure the squared_numbers is printed into the console for the code checking to work.

## List Comprehension 2

You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.

Use List Comprehension instead of a Loop.

Example Output
[2, 8, 34]
Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

Even numbers can be divided by 2 with no remainder.

## List Comprehension 3

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

Create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:

1
2
3
and file2.txt contained:

2
3
4
result = [2, 3]
IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.

Example Output
[3, 6, 5, 33, 12, 7, 42, 13]
Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

First, you will need to read from the files and create a list using the lines in the files.

This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp

Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp

Remember you can convert a string to an int using the int() method. https://www.w3schools.com/python/ref_func_int.asp