# This program merges two dictionaries into a single dictionary.
# If duplicate keys exist, the values from the second dictionary overwrite the first.

dict1 = {"A":10,"B":20}
dict2 = {"B":30,"C":40}

merged = dict1.copy()

for key,value in dict2.items():
    merged[key] = value

print(merged)