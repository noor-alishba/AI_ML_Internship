# This program finds the second largest number in a list
# without using the sort() function.

numbers = [12,45,67,34,89,56]

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print("Second Largest:", second)