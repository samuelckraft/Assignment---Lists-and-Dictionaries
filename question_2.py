#Task 1

def Merge(dict1, dict2):

    merged_dict = dict(dict1.items() | dict2.items())

    return merged_dict

dict1 = {'x': 10, 'y': 8, 'b': 20}
dict2 = {'a': 6, 'b': 4, 'y': 15}

print(Merge(dict1, dict2)) # O(n) complexity, where n is number of key value-pairs

#Task 2

def intersection(d1, d2):
    intersection_dict = {}

    for key, value in d1.items():
        if key in d2:
            intersection_dict[key] = value
    
    return intersection_dict
        


print(intersection(dict1, dict2)) # O(n) complexity, where n is number of key value-pairs


#Task 3

def unique_count(list):
    unique = {}

    for word in list:
        if word in unique:
            unique[word] += 1
        else:
            unique[word] = 1
    
    unique = {key: value for key, value in unique.items() if value < 2}

    return unique

words = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "banana", "cherry"
]

print(unique_count(words)) # O(n) complexity, where n is number of key value-pairs