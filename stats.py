def get_num_words(string):
    text = string.split()
    count = 0
    for i in text:
        count += 1
    return count

def get_count_letter(string):
    text_lower = string.lower()
    result = {}
    for letter in text_lower:
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result

def sorting(dictionary):
    chars_list = []
    for char, count in dictionary.items():
        if char.isalpha():
            chars_list.append({"char": char, "num": count})

    chars_list.sort(reverse=True, key=lambda d: d["num"])

    return chars_list
