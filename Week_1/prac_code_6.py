# Merge Two Dictionaries

dict1 = {"A":10,"B":20}
dict2 = {"B":30,"C":40}

merged = dict1.copy()

for key,value in dict2.items():
    merged[key] = value

print(merged)