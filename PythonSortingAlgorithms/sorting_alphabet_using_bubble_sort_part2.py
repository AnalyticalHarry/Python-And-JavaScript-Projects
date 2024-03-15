# word mapping 
def name_to_numerical_value(name):
    word_mapping = {
        'A': 1, 'a': 1, 'B': 2, 'b': 2, 'C': 3, 'c': 3, 'D': 4, 'd': 4, 'E': 5, 'e': 5,
        'F': 6, 'f': 6, 'G': 7, 'g': 7, 'H': 8, 'h': 8, 'I': 9, 'i': 9, 'J': 10, 'j': 10,
        'K': 11, 'k': 11, 'L': 12, 'l': 12, 'M': 13, 'm': 13, 'N': 14, 'n': 14, 'O': 15, 'o': 15,
        'P': 16, 'p': 16, 'Q': 17, 'q': 17, 'R': 18, 'r': 18, 'S': 19, 's': 19, 'T': 20, 't': 20,
        'U': 21, 'u': 21, 'V': 22, 'v': 22, 'W': 23, 'w': 23, 'X': 24, 'x': 24, 'Y': 25, 'y': 25,
        'Z': 26, 'z': 26
    }
    numerical_value = []
    for i in name:
        if i in word_mapping:
            numerical_value.append(word_mapping[i])
    return numerical_value
    
print(name_to_numerical_value("Hemant Thapa"))
#sorting word in ascending order
def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

print(bubble_sort(name_to_numerical_value("Hemant Thapa")))
# converting array to words
def get_letter_string(numerical_array):
    letter_mapping = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
        6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
        11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
        16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
        21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    }
    letters = [letter_mapping[num] for num in numerical_array]
    return ''.join(letters)

print(get_letter_string(bubble_sort(name_to_numerical_value("Hemant Thapa"))))
