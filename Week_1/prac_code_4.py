# Write a program to Find Second Largest Number


numbers = [12,45,67,34,89,56]

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print("Second Largest:", second)