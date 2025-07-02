def get_num_words(content):
    words = content.split()
    return len(words)

def get_chars_dict(text):
    character_count = {}
    characters = list(text.lower().replace(" ", ""))
    for char in characters:
        if char in character_count:
            character_count[char] = character_count[char] + 1
        else:
            character_count[char] = 1
    return character_count

def chars_dict_to_sorted_list(dictionary):
    char_list = []
    for char in dictionary:
        char_list.append({"char": char, "num": dictionary[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(items):
    return items["num"]