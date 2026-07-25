# This program checks whether a given string is a palindrome or not
# without using Python's slicing method.


text = input("Enter a string: ").lower()

left = 0
right = len(text) - 1

is_palindrome = True

while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")