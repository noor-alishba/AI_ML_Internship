# This program counts the total number of vowels and
# consonants present in a given string.

text = input("Enter a string: ").lower()

vowels = "aeiou"

vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)